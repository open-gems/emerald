
import json
import logging
import time
from uuid import UUID
from uuid6 import uuid7
from asyncpg import Pool
from asyncpg.exceptions import ForeignKeyViolationError, UniqueViolationError
from fastapi import Depends, File, Form, HTTPException, Request, UploadFile, status
from pydantic import BaseModel
from .router import router
from fastapi import UploadFile, HTTPException, status
from infrastructure import S3Service
from fastapi.encoders import ENCODERS_BY_TYPE

ENCODERS_BY_TYPE[bytes] = lambda o: "<binary>"

ALLOWED_MIME_TYPES: dict[str, str] = {
    "application/pdf": "pdf",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document": "docx",
    "text/markdown": "md",
    "text/plain": "txt",
}

MAX_FILE_SIZE_BYTES = 50 * 1024 * 1024  # 50 MB


async def validate_file(file: UploadFile) -> tuple[bytes, str, str]:
    """
    Returns:
        (contents, mime_type, extension)
    Raises:
        HTTPException 415 — unsupported type
        HTTPException 400 — empty file
        HTTPException 413 — exceeds size limit
    """
    if file.content_type not in ALLOWED_MIME_TYPES:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail=(
                f"Tipo de archivo no permitido: '{file.content_type}'. "
                f"Permitidos: {', '.join(ALLOWED_MIME_TYPES.keys())}"
            ),
        )

    contents = await file.read()

    if not contents:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El archivo está vacío.",
        )

    if len(contents) > MAX_FILE_SIZE_BYTES:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail=f"El archivo excede el límite de {MAX_FILE_SIZE_BYTES // (1024 * 1024)} MB.",
        )

    return contents, file.content_type, ALLOWED_MIME_TYPES[file.content_type]

# ── Schema ────────────────────────────────────────────────────

class DocumentResponse(BaseModel):
    id: UUID
    folder_id: UUID
    original_name: str
    internal_name: str
    content_type: str
    mime_type: str
    size_bytes: int
    storage_path: str      
    created_at: int


# ── Query ─────────────────────────────────────────────────────

_INSERT = """
INSERT INTO documents (
    id, user_id, folder_id,
    original_name, internal_name,
    content_type, mime_type,
    size_bytes, storage_path,
    metadata,
    created_at, readed_at, updated_at, deleted_at,
    v
) VALUES (
    $1,  $2,  $3,
    $4,  $5,
    $6,  $7,
    $8,  $9,
    $10,
    $11, NULL, NULL, NULL,
    $12
)
RETURNING
    id, folder_id,
    original_name, internal_name,
    content_type, mime_type,
    size_bytes, storage_path,
    created_at;
"""


def _storage_key(user_id: str, folder_id: str, internal_name: str) -> str:
    """
    S3 object key structure: {user_id}/{folder_id}/{internal_name}
    e.g. "019d2612-.../aef1bc72-....pdf"
    """
    return f"{user_id}/{folder_id}/{internal_name}"

def _build_metadata(original_name: str, size_bytes: int, folder_id: str) -> str:
    """
    JSONB metadata stored alongside the document record.
    Extend freely — this column is the right place for future
    fields (page count, language, virus-scan result, etc.)
    without requiring schema migrations.
    """
    return json.dumps({
        "original_name": original_name,
        "size_bytes":    size_bytes,
        "folder_id":     folder_id,
    })


# ── Endpoint ──────────────────────────────────────────────────

@router.post(
    "/upload-file",
    status_code=status.HTTP_201_CREATED,
    response_model=DocumentResponse,
)
async def upload_file(
    request: Request,
    file: UploadFile = File(...),
    folder_id: str = Form(...),
   
):
    """
    Conservative atomicity strategy:
      1. Upload to SeaweedFS  →  if it fails, DB is untouched.
      2. INSERT into DB       →  if it fails, compensate by deleting from S3.
    """
    logger = request.app.state.logger
    s3 = request.app.state.s3
    pool = request.app.state.pool
    
    logger.debug(f"filename={file.filename!r}")
    logger.debug(f"content_type={file.content_type!r}")
    logger.debug(f"folder_id={folder_id!r}")
    
    contents, raw_content_type, ext = await validate_file(file)

    user_id       = "019d2612-a01d-734c-ab63-917106f31187"  # TODO: authentication
    doc_id        = uuid7()
    original_name = file.filename or f"document.{ext}"
    internal_name = f"{doc_id}.{ext}"
    storage_key   = _storage_key(user_id, folder_id, internal_name)
    created_at    = int(time.time() * 1000)
    metadata      = _build_metadata(original_name, len(contents), folder_id)

    # content_type  → raw HTTP header value, may include params
    #                 e.g. "application/pdf; name=report.pdf"
    # mime_type     → clean MIME type, no params
    #                 e.g. "application/pdf"
    content_type = raw_content_type
    mime_type    = raw_content_type.split(";")[0].strip()

    # ── Phase 1: upload binary ────────────────────────────────
    try:
        await s3.put(
            key=storage_key,
            body=contents,
            content_type=mime_type,
            metadata={
                "document-id":   str(doc_id),
                "folder-id":     folder_id,
                "user-id":       user_id,
                "original-name": original_name,
                "internal-name": internal_name,
            },
        )
        logger.info(f"[upload-document] S3 object written: {storage_key}")
    except Exception as e:
        logger.error(f"[upload-document] SeaweedFS upload failed: {e}")
        raise HTTPException(status.HTTP_502_BAD_GATEWAY, "Error al subir el archivo.")

    # ── Phase 2: persist metadata ─────────────────────────────
    async with pool.acquire() as conn:
        try:
            async with conn.transaction():
                row = await conn.fetchrow(
                    _INSERT,
                    doc_id,        # $1  id
                    user_id,       # $2  user_id
                    folder_id,     # $3  folder_id
                    original_name, # $4  original_name
                    internal_name, # $5  internal_name
                    content_type,  # $6  content_type
                    mime_type,     # $7  mime_type
                    len(contents), # $8  size_bytes
                    storage_key,   # $9  storage_path
                    metadata,      # $10 metadata
                    created_at,    # $11 created_at
                    0,             # $12 v
                )
                if not row:
                    raise RuntimeError("INSERT RETURNING returned empty.")

        except ForeignKeyViolationError:
            await s3.compensate(storage_key, logger)
            raise HTTPException(status.HTTP_404_NOT_FOUND, f"La carpeta '{folder_id}' no existe.")

        except UniqueViolationError:
            await s3.compensate(storage_key, logger)
            raise HTTPException(status.HTTP_409_CONFLICT, "Ya existe un documento con ese identificador.")

        except HTTPException:
            raise

        except Exception as e:
            logger.error(f"[upload-document] DB insert failed: {e}")
            await s3.compensate(storage_key, logger)
            raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, "Error al registrar el documento.")

    # TODO: Dispatch Pub/Sub event


    return DocumentResponse(**dict(row))
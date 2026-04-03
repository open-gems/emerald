from pathlib import Path
from utils import process_pdf_document,format_html

INPUT_PATH = "input"
OUTPUT_PATH = "output"

user_id = "019d2612-a01d-734c-ab63-917106f31187" 

file_name = "019d35cd-3578-7f69-835a-7ad7f2bbe8ec.pdf"

file_path = Path(INPUT_PATH) / user_id / file_name
output_path = Path(OUTPUT_PATH) / user_id 

#html_path, md_path = process_pdf_document(file_path= file_path, output_path=output_path, file_name=file_name)

#format_html(file_path=html_path, output_path=html_path)
        
        
import lmstudio as lms
import asyncio



text = """

Contenido

- TÍTULO 1........................................................................................................................... 7 DISPOSICIONES GENERALES........................................................................................ 7

- CAPÍTULO 1.................................................................................................................. 7 Objeto, ámbito de aplicación y definiciones.................................................................... 7
- CAPÍTULO 2.................................................................................................................. 7 Planeación de la función archivística ............................................................................. 7
- CAPÍTULO 3................................................................................................................ 10 Responsabilidad con los documentos y archivos ......................................................... 10
- CAPÍTULO 4................................................................................................................ 11 Inspección, Vigilancia y Control ................................................................................... 11


- TÍTULO 2......................................................................................................................... 12 ÓRGANOS ASESORES, COORDINADORES Y EJECUTORES DEL SISTEMA NACIONAL DE ARCHIVOS............................................................................................. 12

- CAPÍTULO 1................................................................................................................ 13 Comité Evaluador de Documentos............................................................................... 13
- CAPÍTULO 2................................................................................................................ 15 Archivos Generales Territoriales y Consejos Territoriales de Archivo .......................... 15
- CAPÍTULO 3................................................................................................................ 18 Comités Internos de Archivo........................................................................................ 18


- TÍTULO 3......................................................................................................................... 18 ADMINISTRACIÓN DE ARCHIVOS ................................................................................ 18

- CAPÍTULO 1................................................................................................................ 19 Requisitos para la administración de archivos.............................................................. 19
- CAPÍTULO 2................................................................................................................ 23 Lineamientos generales para la prestación de servicios archivísticos.......................... 23


- TÍTULO 4......................................................................................................................... 23 GESTIÓN DE DOCUMENTOS ........................................................................................ 23


- CAPÍTULO 1................................................................................................................ 24 Planeación y Producción documental .......................................................................... 24
- CAPÍTULO 2................................................................................................................ 25 Gestión y trámite de los documentos ........................................................................... 25
- CAPÍTULO 3................................................................................................................ 29 Principios y criterios para el proceso de organización documental............................... 29

- SECCIÓN 1 ............................................................................................ 29 Organización de archivos: clasificación, ordenación y descripción .................... 29
- SECCIÓN 2 ............................................................................................ 33 Expediente electrónico ............................................................................. 33
- SECCIÓN 3 ............................................................................................ 35 Expediente híbrido ................................................................................... 35


- CAPÍTULO 4............................................................................................................ 36 Transferencias documentales .................................................................................. 36


- CAPÍTULO 5............................................................................................................ 38 Disposición final de los documentos......................................................................... 38


- TÍTULO 5......................................................................................................................... 41 VALORACIÓN DOCUMENTAL........................................................................................ 41

- CAPÍTULO 1................................................................................................................ 41 Tablas de Retención Documental y Tablas de Valoración Documental........................ 41

- SECCIÓN 1.............................................................................................................. 41

Elaboración y aprobación de las Tablas de Retención Documental - TRD y Tablas de Valoración Documental – TVD ................................................................................. 41

- SECCIÓN 2.............................................................................................................. 44

Evaluación y convalidación de Tablas de Retención Documental y Tablas de Valoración Documental............................................................................................ 44

- SECCIÓN 3.............................................................................................................. 48

Inscripción en el Registro Único de Series Documentales – RUSD y publicación de las Tablas de Retención Documental - TRD y Tablas de Valoración Documental – TVD.......................................................................................................................... 48

- SECCIÓN 4.............................................................................................................. 49 Actualización de las Tablas de Retención Documental – TRD ................................. 49
- SECCIÓN 5.............................................................................................................. 51


Implementación de las Tablas de Retención Documental – TRD y Tablas de Valoración Documental – TVD ................................................................................. 51

- CAPÍTULO 2................................................................................................................ 52 Valoración de fondos documentales acumulados ........................................................ 52


- TÍTULO 6......................................................................................................................... 54 CONSERVACIÓN Y PRESERVACIÓN DE DOCUMENTOS........................................... 54

CAPÍTULO 1................................................................................................................ 54 Sistema Integrado de Conservación ............................................................................ 54

- SECCIÓN 1 ............................................................................................ 54 Generalidades ........................................................................................ 54
- SECCIÓN 2 ............................................................................................ 56 Plan de Conservación Documental ............................................................. 56
- SECCIÓN 3 ............................................................................................ 58 Plan de Preservación Digital a Largo Plazo .................................................. 58


- TÍTULO 7......................................................................................................................... 62 ACCESO Y CONSULTA DE LOS DOCUMENTOS.......................................................... 62


- CAPÍTULO 1................................................................................................................ 62 Acceso a la información y los documentos................................................................... 62
- CAPÍTULO 2................................................................................................................ 64 Reproducción de documentos por otros medios técnicos ............................................ 64


- TÍTULO 8......................................................................................................................... 65 PATRIMONIO DOCUMENTAL ........................................................................................ 65

- CAPÍTULO 1................................................................................................................ 65 Registro Nacional de Archivos Históricos Colombianos – RENAHC ............................ 65
- CAPÍTULO 2................................................................................................................ 66 Declaratoria de Bienes de Interés Cultural de Carácter Documental Archivístico -BICCDA............................................................................................................................. 66


- SECCIÓN 1 ............................................................................................ 66 Disposiciones generales ........................................................................... 66
- SECCIÓN 2 ............................................................................................ 68 Procedimiento para la declaratoria de BIC-CDA ............................................ 68
- SECCIÓN 3 ............................................................................................ 70 Lista Indicativa de Candidatos a Bienes de Interés Cultural de Carácter Documental Archivístico – LICBIC-CDA ....................................................... 70
- SECCIÓN 4 ............................................................................................ 72 Régimen Especial de Protección de los Bienes de Interés Cultural de Carácter Documental Archivístico – BIC-CDA ........................................................... 72


CAPITULO 3................................................................................................................ 78 Adquisición y expropiación de archivos privados ......................................................... 78

- SECCIÓN 1.............................................................................................................. 79 Adquisición de archivos privados por donación o compra ........................................ 79
- SECCIÓN 2.............................................................................................................. 80 Expropiación administrativa de archivos privados .................................................... 80


- TÍTULO 9......................................................................................................................... 83 DISPOSICIONES ESPECIALES...................................................................................... 83


- CAPÍTULO 1................................................................................................................ 83 Archivos, Derechos Humanos - DDHH y Derecho Internacional Humanitario DIH ....... 83

- SECCIÓN 1.............................................................................................................. 84

Criterios para la identificación y valoración de documentos relativos a los Derechos Humanos.................................................................................................................. 84

- SECCIÓN 2.............................................................................................................. 85


Criterios para la identificación y valoración de documentos referidos a las graves y manifiestas violaciones a los Derechos Humanos, e infracciones al Derecho Internacional Humanitario, ocurridas con ocasión del conflicto armado interno........ 85

- CAPÍTULO 2................................................................................................................ 87 Archivos fotográficos, sonoros y audiovisuales............................................................ 87
- CAPÍTULO 3................................................................................................................ 88 Reconstrucción de Expedientes................................................................................... 88
- CAPÍTULO 4................................................................................................................ 90 Expedientes Pensionales............................................................................................. 90
- CAPÍTULO 5................................................................................................................ 92


- Historias Laborales ...................................................................................................... 92
- CAPÍTULO 6................................................................................................................ 93 Cámaras de Comercio ................................................................................................. 93
- CAPÍTULO 7................................................................................................................ 94 Licencias urbanísticas y demás documentos que se producen en ejercicio de la función pública asignada a los curadores urbanos por mandato legal...................................... 94


- TÍTULO 10....................................................................................................................... 96 DISPOSICIONES FINALES............................................................................................. 96 ANEXOS DEL ACUERDO ............................................................................................... 98


- ANEXO 1. “Definiciones”.............................................................................................. 98
- ANEXO 2. “Lineamientos generales para la formulación de la Política Institucional de Gestión Documental.” ................................................................................................ 123
- ANEXO 3. “Formato Único de Inventario Documental - FUID” ................................... 130
- ANEXO 4. “Programa de Gestión Documental – PGD”.............................................. 134
- ANEXO 5. “Instructivo y Formato de Cuadro de Clasificación Documental - CCD” .... 136
- ANEXO 6. “Etapas, instructivo y formato - Tablas de Retención Documental – TRD” 139
- ANEXO 7. “Instructivo y formato - Tabla de Valoración Documental – TVD”.............. 144
- ANEXO 8. “Instructivo y formato para descripción de Fondos o Colecciones de documentos fotográficos”........................................................................................... 147
- ANEXO 9. “Instructivo y formato para descripción de Fondos o Colecciones de documentos sonoros”................................................................................................. 151
- ANEXO 10. “Instructivo y formato para descripción de Fondos o Colecciones de documentos audiovisuales”........................................................................................ 155


# EL CONSEJO DIRECTIVO DEL ARCHIVO GENERAL DE LA NACIÓN JORGE PALACIOS PRECIADO

En ejercicio de sus facultades legales, en especial las que le confiere la Ley 80 de 1989, el artículo 76, literal b) de la Ley 489 de 1998, la Ley 594 de 2000, el Decreto 158 de 2022, el Decreto 1080 de 2015, el Acuerdo 09 de 2012 y,

# CONSIDERANDO:

Que el literal b) del artículo 76 de la Ley 489 de 1998, faculta al Consejo Directivo del Archivo General de la Nación para: “Formular a propuestas del representante legal, la política de mejoramiento continuo de la entidad, así como los programas orientados a garantizar el desarrollo administrativo; (…)”.

Que el artículo 1º de la Ley 594 de 2000, establece las reglas y principios generales que regulan la función archivística del país.

- Que, el artículo 3 de la Ley 594 del 2000 define la Función Archivística como las “(…) actividades relacionadas con la totalidad del quehacer archivístico, que comprenden desde la elaboración del documento hasta su eliminación o conservación permanente”, por tanto, incluye todos los procesos de la gestión documental y administración de archivos sin importar el soporte o formato de los documentos.
- Que, el artículo 4 de la mencionada Ley, designa, dentro de los principios generales de la función archivística, al Archivo General de la Nación como la Entidad: “(…) e) del Estado encargada de orientar y coordinar la función archivística para coadyuvar a la eficiencia de la gestión del Estado y salvaguardar el patrimonio documental como parte integral de la riqueza cultural de la Nación, cuya protección es obligación del Estado, según lo dispone el título I de los principios fundamentales de la Constitución Política; (…)”. “(...) g) Los archivos actúan como elementos fundamentales de la racionalidad de la administración pública y como agentes dinamizadores de la acción estatal. Así mismo, constituyen el referente natural de los procesos informativos de aquélla”;” (…).

"""





model = lms.llm("qwen2.5-7b-instruct")

chat = lms.Chat("""
You are a polyglot research assistant. 
Your task is to analyze documents in any language and summarize them.
RULE: Always respond in the SAME language as the original text, 
unless the user explicitly asks for a specific language.
""")

instruccion = f"""
TASK: Analyze and summarize this text in its original language.
SOURCE TEXT: {text}

CONSTRAINTS (STRICT):
1. LANGUAGE: Respond ONLY in the SAME language as the original text.
2. FORMAT: Provide the summary as a SINGLE continuous paragraph.
3. FORBIDDEN: Do NOT include titles, subtitles, bullet points, headers, or bold text. 
4. START: Start the response directly with the summary text.
5. LENGTH: Aim for approximately 500 words.

FINAL WARNING: Output ONLY the raw text of the paragraph. No markdown, no "Sure, here is the summary", no intros.
"""

chat.add_user_message(instruccion) 

configuracion = {
    "maxTokens": 16384, 
    "temperature": 0.8 
}

for fragment in model.respond_stream(chat, config=configuracion):
    print(fragment.content, end="", flush=True)
print()
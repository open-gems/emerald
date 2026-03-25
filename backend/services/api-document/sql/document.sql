CREATE TABLE
    IF NOT EXISTS documents (
        id VARCHAR(50) PRIMARY KEY,
        user_id VARCHAR(50) NOT NULL,
        folder_id VARCHAR(50) NOT NULL,
        file_name VARCHAR(255) NOT NULL,
        internal_name VARCHAR(255) NOT NULL,
        content_type VARCHAR(100) NOT NULL,
        file_size BIGINT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        deleted_at TIMESTAMP DEFAULT NULL,
        v BIGINT NOT NULL,
        CREATE INDEX idx_documents_user_id ON documents(user_id);
    );
CREATE TABLE events (
    id UUID PRIMARY KEY, 
    type           VARCHAR(255) NOT NULL,  
    source         VARCHAR(255) NOT NULL,         
    aggregate_type VARCHAR(255) NOT NULL,             
    aggregate_id   VARCHAR(255) NOT NULL,                           
    data        JSONB           NOT NULL,               
    metadata       JSONB        NOT NULL DEFAULT '{}',
    time           BIGINT       DEFAULT NULL            
    specversion    BIGINT       NOT NULL
);

CREATE INDEX idx_events_created_at     ON events (created_at);
CREATE INDEX idx_events_aggregate      ON events (aggregate_type, aggregate_id);
CREATE INDEX idx_events_type           ON events (type, created_at);


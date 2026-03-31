use crate::{application::EventEnveloped, infrastructure::bootstrap::AppState};
use anyhow::{Context, Result};
use async_trait::async_trait;
use sqlx::{Postgres, Transaction};
use std::sync::Arc;
use tracing::{error};

#[async_trait]
pub trait EventHandlerLogic: Send + Sync {
    // Nuevo: El motor llamará a esto para saber si el handler está interesado
    fn can_handle(&self, entity_type: &str) -> bool;

    async fn handle<'a>(
        &self,
        tx: &mut Transaction<'a, Postgres>,
        event: &EventEnveloped,
    ) -> Result<()>;

    // Ya no es estrictamente necesario si usamos can_handle, 
    // pero podemos dejarlo para logging/identificación.
    fn name(&self) -> &str;
}

pub async fn process_event_with_handler<L: EventHandlerLogic>(
    state: &Arc<AppState>,
    event: &EventEnveloped,
    group: &str,
    logic: &L, // El handler específico del microservicio
) -> Result<bool> {
    // 1. Iniciamos la transacción (Igual que tu código)
    let mut tx = state
        .pool
        .begin()
        .await
        .context("Failed to begin transaction")?;

    let now = chrono::Utc::now().timestamp();

    // 2. Control de duplicados (Idempotencia)
    let result = sqlx::query(
        "INSERT INTO processed (id, consumer_group, event_id, processed_at, status) 
         VALUES ($1, $2, $3, $4, $5) 
         ON CONFLICT (consumer_group, event_id) DO NOTHING",
    )
    .bind(uuid::Uuid::now_v7())
    .bind(group)
    .bind(event.event_id)
    .bind(now)
    .bind("SUCCESS")
    .execute(&mut *tx)
    .await?;

    if result.rows_affected() == 0 {
        return Ok(false); // Ya procesado
    }

    // 3. EJECUCIÓN DINÁMICA: Llamamos al handler del microservicio
    // Pasamos la transacción (&mut *tx) para que sea ATÓMICO
    if let Err(e) = logic.handle(&mut tx, event).await {
        error!(
            "Business logic failed for event {}: {:?}",
            event.event_id, e
        );
        // Al retornar error, no hay commit -> Rollback automático
        return Err(e);
    }

    // 4. Commit final: Se guarda el registro en 'processed' Y lo que hizo el handler
    tx.commit().await.context("Failed to commit transaction")?;

    Ok(true)
}

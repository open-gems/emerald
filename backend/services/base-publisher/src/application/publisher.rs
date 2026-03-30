use crate::{application::ProducerCache, infrastructure::bootstrap::AppState};
use anyhow::Result;
use pulsar::{Pulsar, TokioExecutor};
use serde_json::Value;
use std::sync::Arc;
use tracing::{error, info};
use uuid::Uuid;

#[derive(sqlx::FromRow, Debug)]
struct EventRow {
    id: Uuid,
    entity_type: String,
    data: Value,
}

pub async fn publish_pending_events(
    state: &Arc<AppState>,
    pulsar: &Pulsar<TokioExecutor>,
    producers: &mut ProducerCache,
) -> Result<usize> {
    // 1. Obtener eventos (Usamos SKIP LOCKED para concurrencia segura)
    let rows: Vec<EventRow> = sqlx::query_as::<_, EventRow>(
        "SELECT id, entity_type, data FROM events 
         WHERE published = FALSE 
         ORDER BY time ASC 
         LIMIT $1 FOR UPDATE SKIP LOCKED",
    )
    .bind(state.config.batch_size)
    .fetch_all(&state.pool)
    .await?;

    if rows.is_empty() {
        return Ok(0);
    }

    let mut published_count: usize = 0;

    for row in rows {
        let pattern: String = format!(".{}", row.entity_type);
        let target_topic: &String = state
            .config
            .topics
            .iter()
            .find(|t| t.contains(&pattern))
            .unwrap_or(&state.config.topics[0]);

        if !producers.contains_key(target_topic) {
            let new_producer: pulsar::Producer<TokioExecutor> = pulsar
                .producer()
                .with_topic(target_topic)
                // Opcional: configurar batching aquí para más velocidad
                .build()
                .await?;
            producers.insert(target_topic.clone(), new_producer);
            info!("producer added")
        }

        let producer: &mut pulsar::Producer<TokioExecutor> = producers.get_mut(target_topic).unwrap();

        let payload: Vec<u8> = serde_json::to_vec(&row.data)?;

        match producer.send_non_blocking(payload).await {
            Ok(_) => {
                // 4. Solo si Pulsar confirma, marcamos como publicado en DB
                sqlx::query("UPDATE events SET published = TRUE WHERE id = $1")
                    .bind(row.id)
                    .execute(&state.pool)
                    .await?;
                published_count += 1;

                info!("topic {} - {}", target_topic, row.entity_type);
            }
            Err(e) => error!("Failed to send event {} to pulsar: {:?}", row.id, e),
        }
    }

    Ok(published_count)
}

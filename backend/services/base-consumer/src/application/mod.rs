pub mod consumer;
use crate::{
    application::consumer::{MultiHandler, process_event_with_handler},
    infrastructure::bootstrap::AppState,
};
use anyhow::{Context, Result};
use futures::TryStreamExt;
use pulsar::{
    Consumer, DeserializeMessage, Payload, Pulsar, SubType, TokioExecutor,
    consumer::DeadLetterPolicy,
};
use serde::{Deserialize, Serialize};
use std::sync::Arc;
use tracing::{error, info, warn};
use uuid::Uuid;

#[derive(Serialize, Deserialize, Debug)]
pub struct EventEnveloped {
    pub event_id: Uuid,
    pub event_type: String,
    pub entity_type: String,
    pub data: serde_json::Value,
}

/// Implementation of the `DeserializeMessage` trait to transform Pulsar messages into `EventEnveloped`.
impl DeserializeMessage for EventEnveloped {
    type Output = Result<EventEnveloped, serde_json::Error>;

    fn deserialize_message(payload: &Payload) -> Self::Output {
        serde_json::from_slice(&payload.data)
    }
}

pub async fn run<L>(state: Arc<AppState>, multi_handler: L) -> Result<()>
where
    L: MultiHandler + 'static,
{
    info!("Starting consumer for topics: {:?}", state.config.topics);

    // Initialize the Pulsar client gateway.
    let pulsar: Pulsar<_> = Pulsar::builder(&state.config.pulsar_url, TokioExecutor)
        .build()
        .await
        .context("Failed to create Pulsar client")?;

    // Clone the consumer group name to obtain an owned String.
    let consumer_group: String = state.config.consumer_group.clone();

    // Create a unique name for this consumer.
    let consumer_name: String = format!(
        "{}-{}",
        state.config.consumer_prefix, state.config.consumer_suffix
    );
    
    // Dead Letter Queue (DLQ) Configuration:
    let dlq_policy: DeadLetterPolicy = DeadLetterPolicy {
        max_redeliver_count: 5,
        dead_letter_topic: format!("{}-DLQ", consumer_group),
    };

    // consumer_name : Assign a unique name to this specific instance for tracking.
    // consumer_group: Join the shared subscription group to distribute the workload.
    // KeyShared: to ensure ordered processing by entity ID.
    let mut consumer: Consumer<EventEnveloped, TokioExecutor> = pulsar
        .consumer()
        .with_topics(state.config.topics.clone())
        .with_consumer_name(consumer_name)
        .with_subscription(&consumer_group)
        .with_subscription_type(SubType::KeyShared)
        .with_dead_letter_policy(dlq_policy)
        .build()
        .await?;

    let handlers: Arc<L> = Arc::new(multi_handler);

    while let Some(msg) = consumer.try_next().await? {
        // 1. Deserialize: the payload acknowledging malformed messages to prevent queue blocking.
        let data: EventEnveloped = match msg.deserialize() {
            Ok(data) => data,
            Err(e) => {
                error!("Could not deserialize message: {:?}", e);
                consumer.ack(&msg).await?;
                continue;
            }
        };

        // 2. Early Filtering: Check if the registered handlers can process this entity_type.
        if !handlers.can_handle(&data.entity_type) {
            info!("Event {} ignored by {}", data.event_id, handlers.name());
            consumer.ack(&msg).await?;
            continue;
        }

        // 3. Processing: Attempt to process the event using the transactional handler logic.
        match process_event_with_handler(&state, &data, &consumer_group, &*handlers).await {
            Ok(processed) => {
                if processed {
                    info!(id = %data.event_id, "Event processed successfully");
                } else {
                    warn!(id = %data.event_id, "Event skipped (already processed)");
                }
                consumer.ack(&msg).await?;
            }
            Err(e) => {
                error!(id = %data.event_id, "Critical error processing event: {:?}", e);
                // NACK retry
                consumer.nack(&msg).await?;
            }
        }
    }

    Ok(())
}

use anyhow::Result;
use async_trait::async_trait;
use event_consumer::{
    application::{self, EventEnveloped, consumer::EventHandlerLogic},
    infrastructure::bootstrap::{self, AppState},
};
use sqlx::{Postgres, Transaction};
use tracing::{error, info, warn};

struct FolderHandler;
#[async_trait]
impl EventHandlerLogic for FolderHandler {
    fn can_handle(&self, entity_type: &str) -> bool {
        entity_type == "folder"
    }
    fn name(&self) -> &str {
        "FolderHandler"
    }
    async fn handle<'a>(
        &self,
        tx: &mut Transaction<'a, Postgres>,
        event: &EventEnveloped,
    ) -> Result<()> {
        info!("Processing folder: {}", event.entity_type);
        Ok(())
    }
}
struct MultiHandler {
    folder: FolderHandler,
}

#[async_trait]
impl EventHandlerLogic for MultiHandler {

    fn can_handle(&self, entity_type: &str) -> bool {
        self.folder.can_handle(entity_type)
    }

    fn name(&self) -> &str {
        "MultiHandler"
    }

    async fn handle<'a>(
        &self,
        tx: &mut Transaction<'a, Postgres>,
        event: &EventEnveloped,
    ) -> Result<()> {

        match event.entity_type.as_str() {
            "folder" => self.folder.handle(tx, event).await,
            _ => {
                warn!(
                    "MultiHandler received type it cannot route: {}",
                    event.entity_type
                );
                Ok(())
            }
        }
    }
}

#[tokio::main]
async fn main() -> Result<()> {
    // 1. Bootstrapping: Initialize configuration, database connection pools,
    // and shared resources wrapped in an Arc for thread-safe access.
    let state: std::sync::Arc<AppState> = bootstrap::run().await?;

    // 2. Business Logic Handler: Instance of the specific handler for this service.
    let multi_handler: MultiHandler = MultiHandler {
        folder: FolderHandler,
    };

    // 3. Concurrent Flow Control: 'tokio::select!' monitors multiple futures simultaneously.
    tokio::select! {

    // BRANCH A
    res = application::run(state.clone(), multi_handler) => {
        match res {
            Ok(_) => {
                warn!("Application loop finished gracefully but unexpectedly");
            },
            Err(e) => {
                error!(
                error = %e,
                cause = ?e.source(),
                "Application loop CRASHED"
                );

                return Err(e);
            }
        }
    },
    // BRANCH B
    _ = tokio::signal::ctrl_c() => {
         info!("Ctrl+C signal received, initiating graceful shutdown");
    },
    }

    info!("Service stopped");

    Ok(())
}

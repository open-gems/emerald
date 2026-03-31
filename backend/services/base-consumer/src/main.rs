use anyhow::Result;
use async_trait::async_trait;
use event_consumer::{
    application::{self, EventEnveloped, consumer::EventBusinessLogic},
    infrastructure::bootstrap::{self, AppState},
};
use sqlx::{Postgres, Transaction};
use tracing::{error, info, warn};

struct FolderHandler;

#[async_trait]
impl EventBusinessLogic for FolderHandler {
    fn entity_type(&self) -> &str {
        "folder"
    }

    async fn handle<'a>(
        &self,
        tx: &mut Transaction<'a, Postgres>,
        event: &EventEnveloped,
    ) -> Result<()> {
        
        info!("event consumed");

        Ok(())
    }
}

#[tokio::main]
async fn main() -> Result<()> {
    let state: std::sync::Arc<AppState> = bootstrap::run().await?;

    let handler: FolderHandler = FolderHandler;

    tokio::select! {
    res = application::run(state.clone(), handler) => {
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

    _ = tokio::signal::ctrl_c() => {
         info!("Ctrl+C signal received, initiating graceful shutdown");
    },
    }

    info!("Service stopped");

    Ok(())
}

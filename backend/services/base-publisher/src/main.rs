use anyhow::{Result};
use publisher::{application, infrastructure::bootstrap::{self, AppState}};
use tracing::{error, info};

#[tokio::main]
async fn main() -> Result<()> {
    let state:std::sync::Arc<AppState>  = bootstrap::run().await?;
 
    tokio::select! {
        _ = application::run(state.clone()) => {
            error!("Application loop finished unexpectedly");
        },

        _ = tokio::signal::ctrl_c() => {
            info!("Ctrl+C signal received, initiating graceful shutdown");
        },
    }

    info!("Service stopped");

    Ok(())
}

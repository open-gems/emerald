use anyhow::{Context, Result};
use std::time::Duration;

#[derive(Debug, Clone)]
pub struct Config {
    pub db_url: String,
    pub pulsar_url: String,
    pub batch_size: i64,
    pub poll_interval: Duration,
    pub pulsar_reconnect_delay: Duration,
    pub pulsar_max_retries: u32,
    pub topics: Vec<String>,
    pub pg_max_connections: u32,
    pub pg_acquire_timeout_secs: u64,
    pub pulsar_batch_size: u32,
}

impl Config {
    pub fn from_env() -> Result<Self> {
        let db_url: String = std::env::var("DATABASE_URL").context("DATABASE_URL is not set")?;

        let pulsar_url: String = std::env::var("PULSAR_URL").context("PULSAR_URL is not set")?;

        let batch_size: i64 = std::env::var("BATCH_SIZE")
            .context("BATCH_SIZE is not set")?
            .parse::<i64>()
            .map_err(|_| anyhow::anyhow!("BATCH_SIZE must be a valid integer"))?;

        let poll_interval: Duration = std::env::var("POLL_INTERVAL")
            .context("POLL_INTERVAL is not set")?
            .parse::<u64>()
            .map(|secs: u64| Duration::from_secs(secs))
            .map_err(|_| anyhow::anyhow!("POLL_INTERVAL must be a positive integer"))?;

        let pulsar_reconnect_delay: Duration = std::env::var("PULSAR_RECONNECT_DELAY_SECS")
            .context("PULSAR_RECONNECT_DELAY_SECS is not set")?
            .parse::<u64>()
            .map(Duration::from_secs)
            .map_err(|_| anyhow::anyhow!("PULSAR_RECONNECT_DELAY_SECS must be a valid integer"))?;

        let pulsar_max_retries: u32 = std::env::var("PULSAR_MAX_RETRIES")
            .context("PULSAR_MAX_RETRIES is not set")?
            .parse::<u32>()
            .map_err(|_| anyhow::anyhow!("PULSAR_MAX_RETRIES must be a valid integer"))?;

        let topic_list: String = std::env::var("TOPIC_LIST")
            .context("TOPIC_LIST is not set (expected comma-separated values like a,b,c)")?;

        let topics: Vec<String> = topic_list
            .split(',')
            .map(|s: &str| s.trim().to_string())
            .filter(|s: &String| !s.is_empty())
            .collect();

        let pg_max_connections: u32 = std::env::var("PG_MAX_CONNECTIONS")
            .context("PG_MAX_CONNECTIONS is not set")?
            .parse::<u32>()
            .map_err(|_| anyhow::anyhow!("PG_MAX_CONNECTIONS must be a valid integer"))?;

        let pg_acquire_timeout_secs: u64 = std::env::var("PG_ACQUIRE_TIMEOUT_SECS")
            .context("PG_ACQUIRE_TIMEOUT_SECS is not set")?
            .parse::<u64>()
            .map_err(|_| anyhow::anyhow!("PG_ACQUIRE_TIMEOUT_SECS must be a valid integer"))?;

        let pulsar_batch_size: u32 = std::env::var("PULSAR_BATCH_SIZE")
            .context("PULSAR_BATCH_SIZE is not set")?
            .parse::<u32>()
            .map_err(|_| anyhow::anyhow!("PULSAR_BATCH_SIZE must be a valid integer"))?;

        Ok(Self {
            db_url,
            pulsar_url,
            batch_size,
            poll_interval,
            pulsar_reconnect_delay,
            pulsar_max_retries,
            topics,
            pg_max_connections,
            pg_acquire_timeout_secs,
            pulsar_batch_size,
        })
    }
}

pub fn get_config() -> Result<Config> {
    let config: Config = Config::from_env()?;

    Ok(config)
}

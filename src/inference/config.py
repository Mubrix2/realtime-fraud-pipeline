from pydantic_settings import BaseSettings, SettingsConfigDict

class AppConfigSettings(BaseSettings):
    """Declarative class environment parser mapping type constraints against secret registries."""
    APP_NAME: str = "Enterprise Fraud Inference Engine"
    APP_ENV: str = "development"
    API_PORT: int = 8000

    KAFKA_BOOTSTRAP_SERVERS: str = "localhost:9092"
    KAFKA_TOPIC_NAME: str = "payment-transactions"
    KAFKA_CONSUMER_GROUP_ID: str = "fraud-detection-inference-group"

    # Strict file parsing layout directions loading local variables safely
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

# Instantiated single immutable config data instance across system modules
settings = AppConfigSettings()

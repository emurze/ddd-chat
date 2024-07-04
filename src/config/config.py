from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

from config.log_config import LogLevel


class AppConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="../.env.example",
        extra="allow",
    )

    # FastAPI
    app_title: str = "App"
    allowed_origins: list[str] = [
        "http://localhost:3000",
    ]
    docs_url: str = "/docs"
    redoc_url: str = "/redoc"
    version: str = "0.0.0"
    secret_key: SecretStr
    debug: bool = True
    log_level: LogLevel | None = None

    # MongoDB
    mongodb_connection_dsn: str
    mongodb_chat_database: str
    mongodb_chat_collection: str

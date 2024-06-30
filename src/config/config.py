import logging
from enum import Enum
from typing import Optional

from pydantic import SecretStr, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

LOG_FORMAT_DEBUG = (
    "%(levelname)s:     %(message)s  %(pathname)s:%(funcName)s:%(lineno)d"
)


class LogLevel(str, Enum):
    info = "INFO"
    warning = "WARNING"
    error = "ERROR"
    debug = "DEBUG"


class AppConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file="../.env", extra="ignore")

    # FastAPI
    app_title: str = "App"
    allowed_origins: list[str] = [
        "http://localhost:3000",
    ]
    debug: bool = True
    docs_url: str = "/docs"
    redoc_url: str = "/redoc"
    version: str = "0.0.0"
    secret_key: SecretStr

    # Logging
    log_level_in: Optional[str] = Field(None, validation_alias="log_level")

    @property
    def log_level(self) -> str:
        if self.log_level_in:
            return self.log_level_in.lower()

        if self.debug:
            return LogLevel.debug.lower()

        return LogLevel.warning.lower()

    def configure_logging(self) -> None:
        log_level = self.log_level.upper()
        log_levels = list(LogLevel)

        if log_level not in log_levels:
            # We use LogLevel.error as the default log level
            logging.basicConfig(level=LogLevel.error)
            return

        if log_level == LogLevel.debug:
            logging.basicConfig(level=log_level, format=LOG_FORMAT_DEBUG)
            return

from __future__ import annotations

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = Field(default="llm-p", alias="APP_NAME")
    env: str = Field(default="local", alias="ENV")

    jwt_secret: str = Field(alias="JWT_SECRET")
    jwt_alg: str = Field(default="HS256", alias="JWT_ALG")
    access_token_expire_minutes: int = Field(
        default=60,
        alias="ACCESS_TOKEN_EXPIRE_MINUTES",
    )

    sqlite_path: str = Field(default="./app.db", alias="SQLITE_PATH")

    openrouter_api_key: str = Field(default="", alias="OPENROUTER_API_KEY")
    openrouter_base_url: str = Field(
        default="https://openrouter.ai/api/v1",
        alias="OPENROUTER_BASE_URL",
    )
    openrouter_model: str = Field(alias="OPENROUTER_MODEL")
    openrouter_site_url: str = Field(
        default="https://example.com",
        alias="OPENROUTER_SITE_URL",
    )
    openrouter_app_name: str = Field(
        default="llm-fastapi-openrouter",
        alias="OPENROUTER_APP_NAME",
    )

    cors_enabled: bool = Field(default=True, alias="CORS_ENABLED")
    cors_allow_origins: list[str] = Field(
        default_factory=lambda: ["*"],
        alias="CORS_ALLOW_ORIGINS",
    )


settings = Settings()
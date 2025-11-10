from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix='FASTAPI_')

    database_uri: str = Field(
        'postgres://postgres@postgres@localhost:5432/postgres'
    )

    redis_url: str = Field('redis://localhost:6379/0')

    # Add more settingshere as needed


def get_settings() -> Settings:
    return Settings()  # type:ignore

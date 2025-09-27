from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix='FASTAPI_')

    database_uri: str = Field('postgres://postgres@postgres@localhost:5432/postgres')


@lru_cache()
def get_settings():
    return Settings() #type:ignore

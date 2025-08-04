from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = Field('postgres://postgres@postgres@localhost:5432/postgres')


@lru_cache()
def get_settings():
    return Settings() #type:ignore

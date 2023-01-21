import os
from functools import lru_cache

from pydantic import BaseSettings


class Config(BaseSettings):
    USER = os.environ.get("POSTGRES_USER")
    PASSWORD = os.environ.get("POSTGRES_PASSWORD")
    SERVER = os.environ.get("POSTGRES_SERVER")
    DB = os.environ.get("POSTGRES_DB")

    SQL_DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@app_db/{DB}"


@lru_cache
def get_config() -> Config:
    return Config()


config = get_config()

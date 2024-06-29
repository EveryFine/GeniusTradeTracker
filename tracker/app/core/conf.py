# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     conf
   Description :
   Author :       EveryFine
   Date：          2024/6/22
-------------------------------------------------
   Change Activity:
                   2024/6/22:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

from functools import lru_cache
from typing import Literal

from pydantic import PostgresDsn, computed_field
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', case_sensitive=True)
    # Env Config
    ENVIRONMENT: Literal['dev', 'pro']

    # Env Postgresql
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    @computed_field  # type: ignore[misc]
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> PostgresDsn:
        return MultiHostUrl.build(
            scheme="postgresql+psycopg2",
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_HOST,
            port=self.POSTGRES_PORT,
            path=self.POSTGRES_DB,
        )

    # FastAPI
    TITLE: str = 'TrackerAPI'
    VERSION: str = '0.0.1'
    DESCRIPTION: str = 'Fin Tracker API'
    API_V1_STR: str = '/api/v1'

    # Uvicorn
    UVICORN_HOST: str = '127.0.0.1'
    UVICORN_PORT: int = 8000
    UVICORN_RELOAD: bool = True

    # Middleware
    MIDDLEWARE_ACCESS: bool = True

    # Log
    LOG_STDOUT_FILENAME: str = 'tracker_access.log'
    LOG_STDERR_FILENAME: str = 'tracker_error.log'


@lru_cache
def get_settings():
    """读取配置优化写法"""
    return Settings()


settings = get_settings()

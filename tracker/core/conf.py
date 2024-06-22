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

    # FastAPI
    API_V1_STR: str = '/api/v1'
    TITLE: str = 'TrackerAPI'
    VERSION: str = '0.0.1'
    DESCRIPTION: str = 'Fin Tracker API'

    # Uvicorn
    UVICORN_HOST: str = '127.0.0.1'
    UVICORN_PORT: int = 8000
    UVICORN_RELOAD: bool = True


@lru_cache
def get_settings():
    """读取配置优化写法"""
    return Settings()


settings = get_settings()

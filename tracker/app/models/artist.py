# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     artist
   Description :
   Author :       EveryFine
   Date：          2024/6/29
-------------------------------------------------
   Change Activity:
                   2024/6/29:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

from sqlmodel import SQLModel, Field

from app.models.base import id_key


class Artist(SQLModel, table=True):
    """artist表"""
    artist_id: int = Field(primary_key=True, description='id')
    name: str = Field(max_length=120, description='名称')


class ArtistsPublic(SQLModel):
    data: list[Artist]
    count: int

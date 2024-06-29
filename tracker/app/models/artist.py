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


class ArtistBase(SQLModel):
    name: str = Field(max_length=120, description='名称')

class Artist(ArtistBase, table=True):
    """artist表"""
    artist_id: int | None = Field(default=None,primary_key=True, description='id')

class ArtistCreate(ArtistBase):
    pass

class ArtistPublic(ArtistBase):
    artist_id: int

class ArtistsPublic(SQLModel):
    data: list[Artist]
    count: int

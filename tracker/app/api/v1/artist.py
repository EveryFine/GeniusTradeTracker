# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     employee
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

from fastapi import APIRouter, Query
from sqlmodel import select,func

from app.api.deps import SessionDep
from app.models.artist import ArtistsPublic, Artist

router = APIRouter()


@router.get("/", response_model=ArtistsPublic)
def read_artists(session: SessionDep,
                 offset: int = 0,
                 limit: int = Query(default=100, le=100)):
    count_statement = select(func.count()).select_from(Artist)
    count = session.exec(count_statement).one()

    statement = select(Artist).offset(offset).limit(limit)
    artists = session.exec(statement).all()

    return ArtistsPublic(data=artists, count=count)

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
from app.crud.crud_artist import get_artists, create_artist
from app.models.artist import ArtistsPublic, Artist, ArtistPublic, ArtistCreate

router = APIRouter()


@router.get("/", response_model=ArtistsPublic)
def read_artists(session: SessionDep,
                 offset: int = 0,
                 limit: int = Query(default=100, le=100)):
    artists = get_artists(session=session, offset=offset,limit=limit)

    return artists

@router.post("/", response_model=ArtistPublic)
def create_hero(session: SessionDep, artist: ArtistCreate):
    artist_public = create_artist(session=session, artist_create=artist)
    return artist_public
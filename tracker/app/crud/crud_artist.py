# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     crud_artist
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

from fastapi import Query
from sqlmodel import select, Session,func

from app.models.artist import ArtistsPublic, Artist, ArtistCreate


def get_artists(*, session: Session,  offset: int = 0,limit: int = Query(default=100, le=100)) -> ArtistsPublic:
    count_statement = select(func.count()).select_from(Artist)
    count = session.exec(count_statement).one()

    statement = select(Artist).offset(offset).limit(limit)
    artists = session.exec(statement).all()

    return ArtistsPublic(data=artists, count=count)


def create_artist(*, session: Session, artist_create: ArtistCreate) -> Artist:
    db_artist = Artist.model_validate(artist_create)
    session.add(db_artist)
    session.commit()
    session.refresh(db_artist)
    return db_artist
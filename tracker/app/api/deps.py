# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     deps
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

from typing import Generator, Annotated

from fastapi import Depends
from sqlmodel import Session

from app.core.db import engine


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

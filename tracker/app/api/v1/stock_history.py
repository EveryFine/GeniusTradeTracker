# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_history
   Description :
   Author :       EveryFine
   Date：          2024/7/4
-------------------------------------------------
   Change Activity:
                   2024/7/4:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

from typing import List

from fastapi import APIRouter

from app.api.deps import SessionDep
from app.crud.crud_stock_history import create_stock_histories

router = APIRouter()


@router.post("/", response_model=int)
def create_stock_history(session: SessionDep):
    create_count = create_stock_histories(session=session)
    return create_count

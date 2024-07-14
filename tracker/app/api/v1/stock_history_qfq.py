# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_history_qfq
   Description :
   Author :       EveryFine
   Date：          2024/7/14
-------------------------------------------------
   Change Activity:
                   2024/7/14:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

from fastapi import APIRouter, Query

from app.api.deps import SessionDep
from app.crud.crud_stock_history_qfq import create_stock_histories, create_part_stock_histories

router = APIRouter()


@router.post("/", response_model=int)
def create_stock_history(session: SessionDep):
    create_count = create_stock_histories(session=session)
    return create_count


@router.post("/part", response_model=int)
def create_stock_history(session: SessionDep, stock_offset: int = 0,
                         stock_limit: int = Query(default=100, le=1000)):
    create_count = create_part_stock_histories(session=session, stock_offset=stock_offset, stock_limit=stock_limit)
    return create_count

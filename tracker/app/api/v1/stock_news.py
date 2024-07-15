# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_news
   Description :
   Author :       EveryFine
   Date：          2024/7/15
-------------------------------------------------
   Change Activity:
                   2024/7/15:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

from fastapi import APIRouter, Query

from app.api.deps import SessionDep
from app.crud.crud_stock_news import create_stock_news, create_part_stock_news

router = APIRouter()


@router.post("/", response_model=int)
def create_all_stock_news(session: SessionDep):
    create_count = create_stock_news(session=session)
    return create_count


@router.post("/part", response_model=int)
def create_part_of_stock_news(session: SessionDep, stock_offset: int = 0,
                              stock_limit: int = Query(default=100, le=1000)):
    create_count = create_part_stock_news(session=session, stock_offset=stock_offset, stock_limit=stock_limit)
    return create_count

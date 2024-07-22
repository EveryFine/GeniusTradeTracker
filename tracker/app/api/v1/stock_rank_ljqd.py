# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_rank_ljqd
   Description :  技术指标 -- 量价齐跌
   Author :       EveryFine
   Date：          2024/7/22
-------------------------------------------------
   Change Activity:
                   2024/7/22:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

from fastapi import APIRouter

from app.api.deps import SessionDep
from app.crud.crud_stock_rank_ljqd import create_stock_rank_ljqd

router = APIRouter()


@router.post("/", response_model=int)
def create_all_stock_rank_ljqd(session: SessionDep):
    create_count = create_stock_rank_ljqd(session=session)
    return create_count
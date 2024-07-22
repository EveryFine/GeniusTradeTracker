# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_rank_xzjp
   Description :
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
from app.crud.crud_stock_rank_xzjp import create_stock_rank_xzjp

router = APIRouter()


@router.post("/", response_model=int)
def create_all_stock_rank_xzjp(session: SessionDep):
    create_count = create_stock_rank_xzjp(session=session)
    return create_count
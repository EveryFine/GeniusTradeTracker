# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_rank_xstp
   Description :
   Author :       EveryFine
   Date：          2024/7/21
-------------------------------------------------
   Change Activity:
                   2024/7/21:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

from fastapi import APIRouter

from app.api.deps import SessionDep
from app.crud.crud_stock_rank_xstp import create_stock_rank_xstp

router = APIRouter()


@router.post("/", response_model=int)
def create_all_stock_rank_xstp(session: SessionDep):
    create_count = create_stock_rank_xstp(session=session)
    return create_count

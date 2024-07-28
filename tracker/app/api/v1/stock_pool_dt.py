# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_pool_dt
   Description :
   Author :       EveryFine
   Date：          2024/7/28
-------------------------------------------------
   Change Activity:
                   2024/7/28:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

from fastapi import APIRouter

from app.api.deps import SessionDep
from app.crud.crud_stock_pool_dt import create_stock_pool_dt

router = APIRouter()


@router.post("/", response_model=int)
def create_all_stock_pool_dt(session: SessionDep):
    create_count = create_stock_pool_dt(session=session)
    return create_count

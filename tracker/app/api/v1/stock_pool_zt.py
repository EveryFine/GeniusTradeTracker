# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_pool_zt
   Description :  股池--涨停
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
from app.crud.crud_stock_pool_zt import create_stock_pool_zt

router = APIRouter()

@router.post("/", response_model=int)
def create_all_stock_pool_zt(session: SessionDep):
    create_count = create_stock_pool_zt(session=session)
    return create_count
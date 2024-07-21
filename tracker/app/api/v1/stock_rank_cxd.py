# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_rank_cxd
   Description :  技术指标 -- 创新低
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
from app.crud.crud_stock_rank_cxd import create_stock_rank_cxd

router = APIRouter()


@router.post("/", response_model=int)
def create_all_stock_rank_cxd(session: SessionDep):
    create_count = create_stock_rank_cxd(session=session)
    return create_count

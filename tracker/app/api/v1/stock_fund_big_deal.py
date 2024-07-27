# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_fund_big_deal
   Description :  资金流 -- 大单追踪
   Author :       EveryFine
   Date：          2024/7/27
-------------------------------------------------
   Change Activity:
                   2024/7/27:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

from fastapi import APIRouter

from app.api.deps import SessionDep
from app.crud.crud_stock_fund_big_deal import create_stock_fund_big_deal

router = APIRouter()


@router.post("/", response_model=int)
def create_all_stock_fund_big_deal(session: SessionDep):
    create_count = create_stock_fund_big_deal(session=session)
    return create_count
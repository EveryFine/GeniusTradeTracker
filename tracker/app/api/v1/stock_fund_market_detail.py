# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_fund_market_detail
   Description :   资金流--大盘
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
from app.crud.crud_stock_fund_market_detail import create_stock_fund_market_detail

router = APIRouter()


@router.post("/", response_model=int)
def create_all_stock_fund_market_detail(session: SessionDep):
    create_count = create_stock_fund_market_detail(session=session)
    return create_count

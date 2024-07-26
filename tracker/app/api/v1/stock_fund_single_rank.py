# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_fund_single_rank
   Description :  资金流 -- 个股 -- 排行：3日，5日，10日，20日
   Author :       EveryFine
   Date：          2024/7/26
-------------------------------------------------
   Change Activity:
                   2024/7/26:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

from fastapi import APIRouter

from app.api.deps import SessionDep
from app.crud.crud_stock_fund_single_rank import create_stock_fund_single_ranks

router = APIRouter()


@router.post("/", response_model=int)
def create_all_stock_fund_single_rank(session: SessionDep):
    create_count = create_stock_fund_single_ranks(session=session)
    return create_count

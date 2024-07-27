# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_fund_industry_rank
   Description :
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
from app.crud.crud_stock_fund_industry_rank import create_stock_fund_industry_ranks

router = APIRouter()


@router.post("/", response_model=int)
def create_all_stock_fund_industry_rank(session: SessionDep):
    create_count = create_stock_fund_industry_ranks(session=session)
    return create_count
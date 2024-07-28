# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_fund_industry_detail_intraday
   Description :  资金流--行业--详细--即时
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
from app.crud.crud_stock_fund_industry_detail_intraday import create_stock_fund_industry_detail_intraday

router = APIRouter()


@router.post("/", response_model=int)
def create_all_stock_fund_industry_detail_intraday(session: SessionDep):
    create_count = create_stock_fund_industry_detail_intraday(session=session)
    return create_count
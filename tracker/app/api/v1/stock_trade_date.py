# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_trade_date
   Description :
   Author :       EveryFine
   Date：          2024/7/16
-------------------------------------------------
   Change Activity:
                   2024/7/16:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

from fastapi import APIRouter

from app.api.deps import SessionDep
from app.crud.crud_stock_trade_date import create_stock_trade_dates

router = APIRouter()


@router.post("/", response_model=int)
def create_all_stock_trade_dates(session: SessionDep):
    create_count = create_stock_trade_dates(session=session)
    return create_count

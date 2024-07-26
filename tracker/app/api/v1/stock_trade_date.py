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

import datetime

from fastapi import APIRouter

from app.api.deps import SessionDep
from app.crud.crud_stock_trade_date import create_stock_trade_dates, get_last_trade_date

router = APIRouter()


@router.post("/", response_model=int)
def create_all_stock_trade_dates(session: SessionDep):
    create_count = create_stock_trade_dates(session=session)
    return create_count


@router.get("/", response_model=datetime.date)
def read_last_trade_date(session: SessionDep, datetime: datetime.datetime):
    last_trade_date = get_last_trade_date(session=session, final_datetime=datetime)
    return last_trade_date

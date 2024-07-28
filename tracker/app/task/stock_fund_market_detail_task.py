# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_fund_market_detail_task
   Description :  资金流--大盘
   Author :       EveryFine
   Date：          2024/7/28
-------------------------------------------------
   Change Activity:
                   2024/7/28:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

from datetime import datetime

from sqlmodel import Session

from app.common.log import log
from app.core.db import engine
from app.crud.crud_stock_fund_market_detail import create_stock_fund_market_detail


def execute_create_stock_fund_market_detail():
    log.info(f"{datetime.now()} schedule task [create stock fund market detail] start")
    with Session(engine) as session:
        create_count = create_stock_fund_market_detail(session=session)
        log.info(f"{datetime.now()} schedule task [stock fund market detail] end, create count: {create_count}")

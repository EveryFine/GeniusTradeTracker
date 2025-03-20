# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_fund_single_detail_intraday_task
   Description : 资金流--个股--详细--即时
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
from app.crud.crud_stock_fund_single_detail_intraday import create_stock_fund_single_detail_intraday


def execute_create_stock_fund_single_detail_intraday():
    log.info(f"{datetime.now()} schedule task [create stock fund single detail intraday] start")
    with Session(engine) as session:
        create_count = create_stock_fund_single_detail_intraday(session=session)
        log.info(f"{datetime.now()} schedule task [stock fund single detail intraday] end, create count: {create_count}")

if __name__ == '__main__':
    execute_create_stock_fund_single_detail_intraday()
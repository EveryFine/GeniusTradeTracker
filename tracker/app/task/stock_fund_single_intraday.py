# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_fund_single_intraday
   Description :
   Author :       EveryFine
   Date：          2024/7/25
-------------------------------------------------
   Change Activity:
                   2024/7/25:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

from datetime import datetime
import traceback

from sqlmodel import Session

from app.common.log import log
from app.core.db import engine
from app.crud.crud_stock_fund_single_intraday import create_stock_fund_single_intraday


def execute_create_stock_fund_single_intraday():
    log.info(f"{datetime.now()} schedule task [create stock fund single intraday] start")
    with Session(engine) as session:
        try:
            create_count = create_stock_fund_single_intraday(session=session)
            log.info(f"{datetime.now()} schedule task [stock fund single intraday] end, create count: {create_count}")
        except Exception as e:
            error_msg = f"{datetime.now()} schedule task [stock fund single intraday] error: {str(e)}\n{traceback.format_exc()}"
            log.error(error_msg)

# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_fund_big_deal_task
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

from datetime import datetime
import traceback

from sqlmodel import Session

from app.common.log import log
from app.core.db import engine
from app.crud.crud_stock_fund_big_deal import create_stock_fund_big_deal


def execute_create_stock_fund_big_deal():
    log.info(f"{datetime.now()} schedule task [create stock fund big deal] start")
    with Session(engine) as session:
        try:
            create_count = create_stock_fund_big_deal(session=session)
            log.info(f"{datetime.now()} schedule task [stock fund big deal] end, create count: {create_count}")
        except Exception as e:
            error_msg = f"{datetime.now()} schedule task [stock fund big deal] error: {str(e)}\n{traceback.format_exc()}"
            log.error(error_msg)

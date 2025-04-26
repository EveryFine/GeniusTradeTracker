# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_pool_zt_task
   Description : 股池--涨停
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
import traceback

from sqlmodel import Session

from app.common.log import log
from app.core.db import engine
from app.crud.crud_stock_pool_zt import create_stock_pool_zt


def execute_create_stock_pool_zt():
    log.info(f"{datetime.now()} schedule task [create stock pool zt(股池--涨停)] start")
    with Session(engine) as session:
        try:
            create_count = create_stock_pool_zt(session=session)
            log.info(f"{datetime.now()} schedule task [create stock pool zt(股池--涨停)] end, create count: {create_count}")
        except Exception as e:
            error_msg = f"{datetime.now()} schedule task [create stock pool zt(股池--涨停)] error: {str(e)}\n{traceback.format_exc()}"
            log.error(error_msg)

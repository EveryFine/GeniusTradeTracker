# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_market_activity_realtime_task
   Description :
   Author :       EveryFine
   Date：          2025/11/24
-------------------------------------------------
   Change Activity:
                   2025/11/24:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

from datetime import datetime
import traceback

from sqlmodel import Session

from app.common.log import log
from app.core.db import engine
from app.crud.crud_stock_market_activity_realtime import create_stock_market_activity_realtime


def execute_create_stock_market_activity_realtime():
    log.info(f"{datetime.now()} schedule task [create market activity realtime] start")
    with Session(engine) as session:
        try:
            create_count = create_stock_market_activity_realtime(session=session)
            log.info(
                f"{datetime.now()} schedule task [market activity realtime] end, create count: {create_count}")
        except Exception as e:
            error_msg = f"{datetime.now()} schedule task [market activity realtime] error: {str(e)}\n{traceback.format_exc()}"
            log.error(error_msg)


if __name__ == '__main__':
    execute_create_stock_market_activity_realtime()

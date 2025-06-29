# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_zh_a_spot_em_realtime_task
   Description :
   Author :       EveryFine
   Date：          2025/6/29
-------------------------------------------------
   Change Activity:
                   2025/6/29:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

from datetime import datetime
import traceback

from sqlmodel import Session

from app.common.log import log
from app.core.db import engine
from app.crud.crud_stock_zh_a_spot_em_realtime import create_stock_zh_a_spot_em_realtime


def execute_create_stock_zh_a_spot_em_realtime():
    log.info(f"{datetime.now()} schedule task [create stock stock zh a spot em realtime] start")
    with Session(engine) as session:
        try:
            create_count = create_stock_zh_a_spot_em_realtime(session=session)
            log.info(
                f"{datetime.now()} schedule task [stock stock zh a spot em realtime] end, create count: {create_count}")
        except Exception as e:
            error_msg = f"{datetime.now()} schedule task [stock stock zh a spot em realtime] error: {str(e)}\n{traceback.format_exc()}"
            log.error(error_msg)


if __name__ == '__main__':
    execute_create_stock_zh_a_spot_em_realtime()
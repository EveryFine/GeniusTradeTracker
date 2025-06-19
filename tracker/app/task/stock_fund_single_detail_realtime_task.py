# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_fund_single_detail_realtime_task
   Description :
   Author :       EveryFine
   Date：          2025/6/19
-------------------------------------------------
   Change Activity:
                   2025/6/19:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

from datetime import datetime
import traceback

from sqlmodel import Session

from app.common.log import log
from app.core.db import engine
from app.crud.crud_stock_fund_single_detail_realtime import create_stock_fund_single_detail_realtime


def execute_create_stock_fund_single_detail_realtime():
    log.info(f"{datetime.now()} schedule task [create stock fund single detail realtime] start")
    with Session(engine) as session:
        try:
            create_count = create_stock_fund_single_detail_realtime(session=session)
            log.info(
                f"{datetime.now()} schedule task [stock fund single detail realtime] end, create count: {create_count}")
        except Exception as e:
            error_msg = f"{datetime.now()} schedule task [stock fund single detail realtime] error: {str(e)}\n{traceback.format_exc()}"
            log.error(error_msg)


if __name__ == '__main__':
    execute_create_stock_fund_single_detail_realtime()

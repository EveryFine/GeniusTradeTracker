# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_history_task
   Description : 股票历史行情数据更新任务定义
   Author :       EveryFine
   Date：          2024/7/14
-------------------------------------------------
   Change Activity:
                   2024/7/14:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

from app.common.log import log
from datetime import datetime
from app.crud.crud_stock_history import create_part_stock_histories
from sqlmodel import Session
from app.core.db import engine
import traceback


def execute_create_stock_histories_0_1000():
    log.info(f"{datetime.now()} schedule task [create stock histories 0-1000] start")
    with Session(engine) as session:
        try:
            stock_offset = 0
            stock_limit = 1000
            create_count = create_part_stock_histories(session=session, stock_offset=stock_offset, stock_limit=stock_limit)
            log.info(f"{datetime.now()} schedule task [create stock histories 0-1000] end, create count: {create_count}")
        except Exception as e:
            error_msg = f"{datetime.now()} schedule task [create stock histories 0-1000] error: {str(e)}\n{traceback.format_exc()}"
            log.error(error_msg)


def execute_create_stock_histories_1000_2000():
    log.info(f"{datetime.now()} schedule task [create stock histories 1000-2000] start")
    with Session(engine) as session:
        try:
            stock_offset = 1000
            stock_limit = 1000
            create_count = create_part_stock_histories(session=session, stock_offset=stock_offset, stock_limit=stock_limit)
            log.info(f"{datetime.now()} schedule task [create stock histories 1000-2000] end, create count: {create_count}")
        except Exception as e:
            error_msg = f"{datetime.now()} schedule task [create stock histories 1000-2000] error: {str(e)}\n{traceback.format_exc()}"
            log.error(error_msg)


def execute_create_stock_histories_2000_3000():
    log.info(f"{datetime.now()} schedule task [create stock histories 2000-3000] start")
    with Session(engine) as session:
        try:
            stock_offset = 2000
            stock_limit = 1000
            create_count = create_part_stock_histories(session=session, stock_offset=stock_offset, stock_limit=stock_limit)
            log.info(f"{datetime.now()} schedule task [create stock histories 2000-3000] end, create count: {create_count}")
        except Exception as e:
            error_msg = f"{datetime.now()} schedule task [create stock histories 2000-3000] error: {str(e)}\n{traceback.format_exc()}"
            log.error(error_msg)


def execute_create_stock_histories_3000_4000():
    log.info(f"{datetime.now()} schedule task [create stock histories 3000-4000] start")
    with Session(engine) as session:
        try:
            stock_offset = 3000
            stock_limit = 1000
            create_count = create_part_stock_histories(session=session, stock_offset=stock_offset, stock_limit=stock_limit)
            log.info(f"{datetime.now()} schedule task [create stock histories 3000-4000] end, create count: {create_count}")
        except Exception as e:
            error_msg = f"{datetime.now()} schedule task [create stock histories 3000-4000] error: {str(e)}\n{traceback.format_exc()}"
            log.error(error_msg)


def execute_create_stock_histories_4000_5000():
    log.info(f"{datetime.now()} schedule task [create stock histories 4000-5000] start")
    with Session(engine) as session:
        try:
            stock_offset = 4000
            stock_limit = 1000
            create_count = create_part_stock_histories(session=session, stock_offset=stock_offset, stock_limit=stock_limit)
            log.info(f"{datetime.now()} schedule task [create stock histories 4000-5000] end, create count: {create_count}")
        except Exception as e:
            error_msg = f"{datetime.now()} schedule task [create stock histories 4000-5000] error: {str(e)}\n{traceback.format_exc()}"
            log.error(error_msg)


if __name__ == '__main__':
    execute_create_stock_histories_0_1000()

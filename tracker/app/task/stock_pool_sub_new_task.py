# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_pool_sub_new_task
   Description :
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
from app.crud.crud_stock_pool_sub_new import create_stock_pool_sub_new


def execute_create_stock_pool_sub_new():
    log.info(f"{datetime.now()} schedule task [create stock pool sub new(股池--次新)] start")
    with Session(engine) as session:
        try:
            create_count = create_stock_pool_sub_new(session=session)
            log.info(f"{datetime.now()} schedule task [create stock pool sub new(股池--次新)] end, create count: {create_count}")
        except Exception as e:
            error_msg = f"{datetime.now()} schedule task [create stock pool sub new(股池--次新)] error: {str(e)}\n{traceback.format_exc()}"
            log.error(error_msg)


if __name__ == '__main__':
    execute_create_stock_pool_sub_new()
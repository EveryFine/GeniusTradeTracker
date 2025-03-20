# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_pool_zb_task
   Description :   股池--炸板
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
from app.crud.crud_stock_pool_zb import create_stock_pool_zb


def execute_create_stock_pool_zb():
    log.info(f"{datetime.now()} schedule task [create stock pool zb(股池--炸板)] start")
    with Session(engine) as session:
        create_count = create_stock_pool_zb(session=session)
        log.info(f"{datetime.now()} schedule task [create stock pool zb(股池--炸板)] end, create count: {create_count}")

if __name__ == '__main__':
    execute_create_stock_pool_zb()
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_pool_strong_task
   Description :  股池--强势
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
from app.crud.crud_stock_pool_strong import create_stock_pool_strong


def execute_create_stock_pool_strong():
    log.info(f"{datetime.now()} schedule task [create stock pool strong(股池--强势)] start")
    with Session(engine) as session:
        create_count = create_stock_pool_strong(session=session)
        log.info(f"{datetime.now()} schedule task [create stock pool strong(股池--强势)] end, create count: {create_count}")

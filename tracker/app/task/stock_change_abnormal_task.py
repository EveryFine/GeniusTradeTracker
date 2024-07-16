# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_change_abnormal_task
   Description :
   Author :       EveryFine
   Date：          2024/7/16
-------------------------------------------------
   Change Activity:
                   2024/7/16:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

from datetime import datetime

from sqlmodel import Session

from app.common.log import log
from app.core.db import engine
from app.crud.crud_stock_change_abnormal import create_stock_change_abnormal


def execute_create_stock_change_abnormal():
    log.info(f"{datetime.now()} schedule task [create stock change abnormal] start")
    with Session(engine) as session:
        create_count = create_stock_change_abnormal(session=session)
        log.info(f"{datetime.now()} schedule task [create stock change abnormal] end, create count: {create_count}")

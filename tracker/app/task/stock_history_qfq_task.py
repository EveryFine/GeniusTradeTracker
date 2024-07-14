# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_history_qfq_task
   Description :
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
from app.crud.crud_stock_history_qfq import create_part_stock_histories
from sqlmodel import Session
from app.core.db import engine


def execute_create_stock_histories_qfq_0_1000():
    log.info(f"{datetime.now()} schedule task [create stock histories qfq 0-1000] start")
    with Session(engine) as session:
        stock_offset = 0
        stock_limit = 1000
        create_count = create_part_stock_histories(session=session, stock_offset=stock_offset, stock_limit=stock_limit)
        log.info(f"{datetime.now()} schedule task [create stock histories qfq 0-1000] end, create count: {create_count}")


def execute_create_stock_histories_qfq_1000_2000():
    log.info(f"{datetime.now()} schedule task [create stock histories qfq 1000-2000] start")
    with Session(engine) as session:
        stock_offset = 1000
        stock_limit = 1000
        create_count = create_part_stock_histories(session=session, stock_offset=stock_offset, stock_limit=stock_limit)
        log.info(f"{datetime.now()} schedule task [create stock histories qfq 1000-2000] end, create count: {create_count}")


def execute_create_stock_histories_qfq_2000_3000():
    log.info(f"{datetime.now()} schedule task [create stock histories qfq 2000-3000] start")
    with Session(engine) as session:
        stock_offset = 2000
        stock_limit = 1000
        create_count = create_part_stock_histories(session=session, stock_offset=stock_offset, stock_limit=stock_limit)
        log.info(f"{datetime.now()} schedule task [create stock histories qfq 2000-3000] end, create count: {create_count}")


def execute_create_stock_histories_qfq_3000_4000():
    log.info(f"{datetime.now()} schedule task [create stock histories qfq 3000-4000] start")
    with Session(engine) as session:
        stock_offset = 3000
        stock_limit = 1000
        create_count = create_part_stock_histories(session=session, stock_offset=stock_offset, stock_limit=stock_limit)
        log.info(f"{datetime.now()} schedule task [create stock histories qfq 3000-4000] end, create count: {create_count}")


def execute_create_stock_histories_qfq_4000_5000():
    log.info(f"{datetime.now()} schedule task [create stock histories qfq 4000-5000] start")
    with Session(engine) as session:
        stock_offset = 4000
        stock_limit = 1000
        create_count = create_part_stock_histories(session=session, stock_offset=stock_offset, stock_limit=stock_limit)
        log.info(f"{datetime.now()} schedule task [create stock histories qfq 4000-5000] end, create count: {create_count}")

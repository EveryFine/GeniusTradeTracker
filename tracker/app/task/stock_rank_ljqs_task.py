# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_rank_ljqs_task
   Description :   技术指标 -- 量价齐升
   Author :       EveryFine
   Date：          2024/7/22
-------------------------------------------------
   Change Activity:
                   2024/7/22:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

from datetime import datetime

from sqlmodel import Session

from app.common.log import log
from app.core.db import engine
from app.crud.crud_stock_rank_ljqs import create_stock_rank_ljqs


def execute_create_stock_rank_ljqs():
    log.info(f"{datetime.now()} schedule task [create stock rank ljqs] start")
    with Session(engine) as session:
        create_count = create_stock_rank_ljqs(session=session)
        log.info(f"{datetime.now()} schedule task [create stock rank ljqs] end, create count: {create_count}")

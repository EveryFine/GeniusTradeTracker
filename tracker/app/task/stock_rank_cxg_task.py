# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_rank_cxg_task
   Description :
   Author :       EveryFine
   Date：          2024/7/21
-------------------------------------------------
   Change Activity:
                   2024/7/21:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

from datetime import datetime

from sqlmodel import Session

from app.common.log import log
from app.core.db import engine
from app.crud.crud_stock_rank_cxg import create_stock_rank_cxg


def execute_create_stock_rank_cxg():
    log.info(f"{datetime.now()} schedule task [create stock rank cxg] start")
    with Session(engine) as session:
        create_count = create_stock_rank_cxg(session=session)
        log.info(f"{datetime.now()} schedule task [create stock rank cxg] end, create count: {create_count}")

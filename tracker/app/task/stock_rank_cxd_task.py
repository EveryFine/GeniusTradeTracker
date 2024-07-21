# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_rank_cxd_task
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
from app.crud.crud_stock_rank_cxd import create_stock_rank_cxd


def execute_create_stock_rank_cxd():
    log.info(f"{datetime.now()} schedule task [create stock rank cxd] start")
    with Session(engine) as session:
        create_count = create_stock_rank_cxd(session=session)
        log.info(f"{datetime.now()} schedule task [create stock rank cxd] end, create count: {create_count}")

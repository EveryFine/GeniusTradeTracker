# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_fund_industry_rank_task
   Description :
   Author :       EveryFine
   Date：          2024/7/27
-------------------------------------------------
   Change Activity:
                   2024/7/27:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

from datetime import datetime

from sqlmodel import Session

from app.common.log import log
from app.core.db import engine
from app.crud.crud_stock_fund_industry_rank import create_stock_fund_industry_ranks


def execute_create_stock_fund_industry_rank():
    log.info(f"{datetime.now()} schedule task [create stock fund industry rank] start")
    with Session(engine) as session:
        create_count = create_stock_fund_industry_ranks(session=session)
        log.info(f"{datetime.now()} schedule task [stock fund industry rank] end, create count: {create_count}")

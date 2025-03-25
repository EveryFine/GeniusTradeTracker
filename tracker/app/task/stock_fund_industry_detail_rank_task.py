# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_fund_industry_detail_rank_task
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

from sqlmodel import Session

from app.common.log import log
from app.core.db import engine
from app.crud.crud_stock_fund_industry_detail_rank import create_stock_fund_industry_detail_rank


def execute_create_stock_fund_industry_detail_rank():
    log.info(f"{datetime.now()} schedule task [create stock fund industry detail rank] start")
    with Session(engine) as session:
        create_count = create_stock_fund_industry_detail_rank(session=session)
        log.info(f"{datetime.now()} schedule task [stock fund industry detail rank] end, create count: {create_count}")

if __name__ == '__main__':
    execute_create_stock_fund_industry_detail_rank()
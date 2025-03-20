# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_fund_single_detail_rank_task
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
from app.crud.crud_stock_fund_single_detail_rank import create_stock_fund_single_detail_rank, \
    create_stock_fund_single_detail_rank_by_types


def execute_create_stock_fund_single_detail_rank():
    log.info(f"{datetime.now()} schedule task [create stock fund single detail rank] start")
    with Session(engine) as session:
        create_count = create_stock_fund_single_detail_rank(session=session)
        # create_count = create_stock_fund_single_detail_rank_by_types(session, ['10日'])
        log.info(f"{datetime.now()} schedule task [stock fund single detail rank] end, create count: {create_count}")

if __name__ == '__main__':
    execute_create_stock_fund_single_detail_rank()
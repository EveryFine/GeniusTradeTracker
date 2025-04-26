# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_fund_concept_detail_rank_task
   Description :   资金流--概念--详细--排行
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
import traceback

from sqlmodel import Session

from app.common.log import log
from app.core.db import engine
from app.crud.crud_stock_fund_concept_detail_rank import create_stock_fund_concept_detail_rank


def execute_create_stock_fund_concept_detail_rank():
    log.info(f"{datetime.now()} schedule task [create stock fund concept detail rank] start")
    with Session(engine) as session:
        try:
            create_count = create_stock_fund_concept_detail_rank(session=session)
            log.info(f"{datetime.now()} schedule task [stock fund concept detail rank] end, create count: {create_count}")
        except Exception as e:
            error_msg = f"{datetime.now()} schedule task [stock fund concept detail rank] error: {str(e)}\n{traceback.format_exc()}"
            log.error(error_msg)


if __name__ == '__main__':
    execute_create_stock_fund_concept_detail_rank()
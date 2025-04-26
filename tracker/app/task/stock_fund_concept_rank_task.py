# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_fund_concept_rank_task
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
import traceback

from sqlmodel import Session

from app.common.log import log
from app.core.db import engine
from app.crud.crud_stock_fund_concept_rank import create_stock_fund_concept_ranks


def execute_create_stock_fund_concept_rank():
    log.info(f"{datetime.now()} schedule task [create stock fund concept rank] start")
    with Session(engine) as session:
        try:
            create_count = create_stock_fund_concept_ranks(session=session)
            log.info(f"{datetime.now()} schedule task [stock fund concept rank] end, create count: {create_count}")
        except Exception as e:
            error_msg = f"{datetime.now()} schedule task [stock fund concept rank] error: {str(e)}\n{traceback.format_exc()}"
            log.error(error_msg)

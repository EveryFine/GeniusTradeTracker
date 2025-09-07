# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_board_industry_em_task
   Description :
   Author :       EveryFine
   Date：          2025/9/7
-------------------------------------------------
   Change Activity:
                   2025/9/7:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

import traceback
from datetime import datetime

from sqlmodel import Session

from app.common.log import log
from app.core.db import engine
from app.crud.crud_stock_board_industry_em import create_stock_board_industry_em


def execute_create_stock_board_industry_em():
    log.info(f"{datetime.now()} schedule task [create stock board industry em(东方财富-行业板块)] start")
    with Session(engine) as session:
        try:
            create_count = create_stock_board_industry_em(session=session)
            log.info(
                f"{datetime.now()} schedule task [create stock board industry em(东方财富-行业板块)] end, create count: {create_count}")
        except Exception as e:
            error_msg = f"{datetime.now()} schedule task [create stock board industry em(东方财富-行业板块)] error: {str(e)}\n{traceback.format_exc()}"
            log.error(error_msg)
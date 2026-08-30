# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_board_industry_cons_em_task
   Description :   Task to create industry board constituent records
   Author :       EveryFine
   Date：          2026/08/30
-------------------------------------------------
"""
__author__ = 'EveryFine'

import traceback
from datetime import datetime

from sqlmodel import Session

from app.common.log import log
from app.core.db import engine
from app.crud.crud_stock_board_industry_cons_em import create_stock_board_industry_cons_em


def execute_create_stock_board_industry_cons_em():
    log.info(f"{datetime.now()} schedule task [create stock board industry cons em(东方财富-行业板块-板块成份)] start")
    with Session(engine) as session:
        try:
            create_count = create_stock_board_industry_cons_em(session=session)
            log.info(
                f"{datetime.now()} schedule task [create stock board industry cons em(东方财富-行业板块-板块成份)] end, create count: {create_count}")
        except Exception as e:
            error_msg = f"{datetime.now()} schedule task [create stock board industry cons em(东方财富-行业板块-板块成份)] error: {str(e)}\n{traceback.format_exc()}"
            log.error(error_msg)


if __name__ == '__main__':
    execute_create_stock_board_industry_cons_em()

# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_board_change_em_task
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
from app.crud.crud_stock_board_change_em import create_stock_board_change_em


def execute_create_stock_board_change_em():
    log.info(f"{datetime.now()} schedule task [create stock board change em(东方财富-行情中心-当日板块异动详情)] start")
    with Session(engine) as session:
        try:
            create_count = create_stock_board_change_em(session=session)
            log.info(
                f"{datetime.now()} schedule task [create stock board change em(东方财富-行情中心-当日板块异动详情)] end, create count: {create_count}")
        except Exception as e:
            error_msg = f"{datetime.now()} schedule task [create stock board change em(东方财富-行情中心-当日板块异动详情)] error: {str(e)}\n{traceback.format_exc()}"
            log.error(error_msg)
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_board_concept_em_realtime_realtime_task
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
from app.crud.crud_stock_board_concept_em_realtime import create_stock_board_concept_em_realtime


def execute_create_stock_board_concept_em_realtime():
    log.info(f"{datetime.now()} schedule task [create stock board concept em realtime(东方财富-概念板块-实时)] start")
    with Session(engine) as session:
        try:
            create_count = create_stock_board_concept_em_realtime(session=session)
            log.info(
                f"{datetime.now()} schedule task [create stock board concept em realtime(东方财富-概念板块-实时)] end, create count: {create_count}")
        except Exception as e:
            error_msg = f"{datetime.now()} schedule task [create stock board concept em realtime(东方财富-概念板块-实时)] error: {str(e)}\n{traceback.format_exc()}"
            log.error(error_msg)
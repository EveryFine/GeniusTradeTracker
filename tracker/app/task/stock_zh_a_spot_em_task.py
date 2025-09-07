# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_zh_a_spot_em_task
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

from datetime import datetime
import traceback

from sqlmodel import Session

from app.common.log import log
from app.core.db import engine
from app.crud.crud_stock_zh_a_spot_em import create_stock_zh_a_spot_em


def execute_create_stock_zh_a_spot_em():
    log.info(f"{datetime.now()} schedule task [create stock stock zh a spot em] start")
    with Session(engine) as session:
        try:
            create_count = create_stock_zh_a_spot_em(session=session)
            log.info(
                f"{datetime.now()} schedule task [stock stock zh a spot em] end, create count: {create_count}")
        except Exception as e:
            error_msg = f"{datetime.now()} schedule task [stock stock zh a spot em] error: {str(e)}\n{traceback.format_exc()}"
            log.error(error_msg)
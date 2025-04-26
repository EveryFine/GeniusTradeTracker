# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_rank_ljqd_task
   Description :
   Author :       EveryFine
   Date：          2024/7/22
-------------------------------------------------
   Change Activity:
                   2024/7/22:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

import traceback
from datetime import datetime

from sqlmodel import Session

from app.common.log import log
from app.core.db import engine
from app.crud.crud_stock_rank_ljqd import create_stock_rank_ljqd


def execute_create_stock_rank_ljqd():
    log.info(f"{datetime.now()} schedule task [create stock rank ljqd] start")
    with Session(engine) as session:
        try:
            create_count = create_stock_rank_ljqd(session=session)
            log.info(f"{datetime.now()} schedule task [create stock rank ljqd] end, create count: {create_count}")
        except Exception as e:
            error_msg = f"{datetime.now()} schedule task [create stock rank ljqd] error: {str(e)}\n{traceback.format_exc()}"
            log.error(error_msg)
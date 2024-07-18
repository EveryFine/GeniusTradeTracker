# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_comment_task
   Description :
   Author :       EveryFine
   Date：          2024/7/18
-------------------------------------------------
   Change Activity:
                   2024/7/18:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

from datetime import datetime

from sqlmodel import Session

from app.common.log import log
from app.core.db import engine
from app.crud.crud_stock_comment import create_stock_comments


def execute_create_stock_comment():
    log.info(f"{datetime.now()} schedule task [create stock comments] start")
    with Session(engine) as session:
        create_count = create_stock_comments(session=session)
        log.info(f"{datetime.now()} schedule task [create stock comments] end, create count: {create_count}")

# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_company_event_task
   Description :
   Author :       EveryFine
   Date：          2024/7/21
-------------------------------------------------
   Change Activity:
                   2024/7/21:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

from datetime import datetime

from sqlmodel import Session

from app.common.log import log
from app.core.db import engine
from app.crud.crud_stock_company_event import create_all_stock_company_events


def execute_create_stock_company_event():
    log.info(f"{datetime.now()} schedule task [create stock company events] start")
    with Session(engine) as session:
        create_count = create_all_stock_company_events(session=session)
        log.info(f"{datetime.now()} schedule task [create stock company events] end, create count: {create_count}")

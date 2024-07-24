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

from datetime import datetime, date

from sqlmodel import Session

from app.common.log import log
from app.core.db import engine
from app.crud.crud_stock_company_event import create_all_stock_company_events, create_part_stock_company_events


def execute_create_stock_company_event():
    log.info(f"{datetime.now()} schedule task [create stock company events] start")
    with Session(engine) as session:
        start_date = date(2024, 6, 24)
        end_date = date.today()
        create_count = create_part_stock_company_events(session=session, start_date=start_date, end_date=end_date)
        log.info(f"{datetime.now()} schedule task [create stock company events] end, create count: {create_count}")

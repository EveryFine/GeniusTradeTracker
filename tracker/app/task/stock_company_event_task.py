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
import traceback

from sqlmodel import Session

from app.common.log import log
from app.core.db import engine
from app.crud.crud_stock_company_event import create_all_stock_company_events, create_part_stock_company_events


def execute_create_stock_company_event():
    log.info(f"{datetime.now()} schedule task [create stock company events] start")
    with Session(engine) as session:
        try:
            start_date = date(2024, 8, 1)
            end_date = date.today()
            create_count = create_part_stock_company_events(session=session, start_date=start_date, end_date=end_date)
            log.info(f"{datetime.now()} schedule task [create stock company events] end, create count: {create_count}")
        except Exception as e:
            error_msg = f"{datetime.now()} schedule task [create stock company events] error: {str(e)}\n{traceback.format_exc()}"
            log.error(error_msg)

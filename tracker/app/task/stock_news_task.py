# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_news_task
   Description :
   Author :       EveryFine
   Date：          2024/7/15
-------------------------------------------------
   Change Activity:
                   2024/7/15:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

from datetime import datetime
import traceback

from sqlmodel import Session

from app.common.log import log
from app.core.db import engine
from app.crud.crud_stock_news import create_part_stock_news


def execute_create_stock_news_0_1000():
    log.info(f"{datetime.now()} schedule task [create stock news 0-1000] start")
    with Session(engine) as session:
        try:
            stock_offset = 0
            stock_limit = 1000
            create_count = create_part_stock_news(session=session, stock_offset=stock_offset, stock_limit=stock_limit)
            log.info(f"{datetime.now()} schedule task [create stock news 0-1000] end, create count: {create_count}")
        except Exception as e:
            error_msg = f"{datetime.now()} schedule task [create stock news 0-1000] error: {str(e)}\n{traceback.format_exc()}"
            log.error(error_msg)


def execute_create_stock_news_1000_2000():
    log.info(f"{datetime.now()} schedule task [create stock news 1000-2000] start")
    with Session(engine) as session:
        try:
            stock_offset = 1000
            stock_limit = 1000
            create_count = create_part_stock_news(session=session, stock_offset=stock_offset, stock_limit=stock_limit)
            log.info(f"{datetime.now()} schedule task [create stock news 1000-2000] end, create count: {create_count}")
        except Exception as e:
            error_msg = f"{datetime.now()} schedule task [create stock news 1000-2000] error: {str(e)}\n{traceback.format_exc()}"
            log.error(error_msg)


def execute_create_stock_news_2000_3000():
    log.info(f"{datetime.now()} schedule task [create stock news 2000-3000] start")
    with Session(engine) as session:
        try:
            stock_offset = 2000
            stock_limit = 1000
            create_count = create_part_stock_news(session=session, stock_offset=stock_offset, stock_limit=stock_limit)
            log.info(f"{datetime.now()} schedule task [create stock news 2000-3000] end, create count: {create_count}")
        except Exception as e:
            error_msg = f"{datetime.now()} schedule task [create stock news 2000-3000] error: {str(e)}\n{traceback.format_exc()}"
            log.error(error_msg)


def execute_create_stock_news_3000_4000():
    log.info(f"{datetime.now()} schedule task [create stock news 3000-4000] start")
    with Session(engine) as session:
        try:
            stock_offset = 3000
            stock_limit = 1000
            create_count = create_part_stock_news(session=session, stock_offset=stock_offset, stock_limit=stock_limit)
            log.info(f"{datetime.now()} schedule task [create stock news 3000-4000] end, create count: {create_count}")
        except Exception as e:
            error_msg = f"{datetime.now()} schedule task [create stock news 3000-4000] error: {str(e)}\n{traceback.format_exc()}"
            log.error(error_msg)


def execute_create_stock_news_4000_5000():
    log.info(f"{datetime.now()} schedule task [create stock news 4000-5000] start")
    with Session(engine) as session:
        try:
            stock_offset = 4000
            stock_limit = 1000
            create_count = create_part_stock_news(session=session, stock_offset=stock_offset, stock_limit=stock_limit)
            log.info(f"{datetime.now()} schedule task [create stock news 4000-5000] end, create count: {create_count}")
        except Exception as e:
            error_msg = f"{datetime.now()} schedule task [create stock news 4000-5000] error: {str(e)}\n{traceback.format_exc()}"
            log.error(error_msg)

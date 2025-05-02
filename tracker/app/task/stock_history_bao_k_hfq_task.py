# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_history_bao_k_hfq_task
   Description :
   Author :       EveryFine
   Date：          2025/5/2
-------------------------------------------------
   Change Activity:
                   2025/5/2:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

from app.common.log import log
from datetime import datetime
from app.crud.crud_stock_history_bao_k_hfq import create_part_stock_bao_k_hfq
from sqlmodel import Session
from app.core.db import engine
import traceback


def execute_create_stock_history_bao_k_hfq_0_1000():
    log.info(f"{datetime.now()} schedule task [create stock history bao k hfq 0-1000] start")
    with Session(engine) as session:
        try:
            stock_offset = 0
            stock_limit = 1000
            create_count = create_part_stock_bao_k_hfq(session=session, stock_offset=stock_offset,
                                                       stock_limit=stock_limit)
            log.info(
                f"{datetime.now()} schedule task [create stock history bao k hfq 0-1000] end, create count: {create_count}")
        except Exception as e:
            error_msg = f"{datetime.now()} schedule task [create stock history bao k hfq 0-1000] error: {str(e)}\n{traceback.format_exc()}"
            log.error(error_msg)


def execute_create_stock_history_bao_k_hfq_1000_2000():
    log.info(f"{datetime.now()} schedule task [create stock history bao k hfq 1000-2000] start")
    with Session(engine) as session:
        try:
            stock_offset = 1000
            stock_limit = 1000
            create_count = create_part_stock_bao_k_hfq(session=session, stock_offset=stock_offset,
                                                       stock_limit=stock_limit)
            log.info(
                f"{datetime.now()} schedule task [create stock history bao k hfq 1000-2000] end, create count: {create_count}")
        except Exception as e:
            error_msg = f"{datetime.now()} schedule task [create stock history bao k hfq 1000-2000] error: {str(e)}\n{traceback.format_exc()}"
            log.error(error_msg)


def execute_create_stock_history_bao_k_hfq_2000_3000():
    log.info(f"{datetime.now()} schedule task [create stock history bao k hfq 2000-3000] start")
    with Session(engine) as session:
        try:
            stock_offset = 2000
            stock_limit = 1000
            create_count = create_part_stock_bao_k_hfq(session=session, stock_offset=stock_offset,
                                                       stock_limit=stock_limit)
            log.info(
                f"{datetime.now()} schedule task [create stock history bao k hfq 2000-3000] end, create count: {create_count}")
        except Exception as e:
            error_msg = f"{datetime.now()} schedule task [create stock history bao k hfq 2000-3000] error: {str(e)}\n{traceback.format_exc()}"
            log.error(error_msg)


def execute_create_stock_history_bao_k_hfq_3000_4000():
    log.info(f"{datetime.now()} schedule task [create stock history bao k hfq 3000-4000] start")
    with Session(engine) as session:
        try:
            stock_offset = 3000
            stock_limit = 1000
            create_count = create_part_stock_bao_k_hfq(session=session, stock_offset=stock_offset,
                                                       stock_limit=stock_limit)
            log.info(
                f"{datetime.now()} schedule task [create stock history bao k hfq 3000-4000] end, create count: {create_count}")
        except Exception as e:
            error_msg = f"{datetime.now()} schedule task [create stock history bao k hfq 3000-4000] error: {str(e)}\n{traceback.format_exc()}"
            log.error(error_msg)


def execute_create_stock_history_bao_k_hfq_4000_5000():
    log.info(f"{datetime.now()} schedule task [create stock history bao k hfq 4000-5000] start")
    with Session(engine) as session:
        try:
            stock_offset = 4000
            stock_limit = 1000
            create_count = create_part_stock_bao_k_hfq(session=session, stock_offset=stock_offset,
                                                       stock_limit=stock_limit)
            log.info(
                f"{datetime.now()} schedule task [create stock history bao k hfq 4000-5000] end, create count: {create_count}")
        except Exception as e:
            error_msg = f"{datetime.now()} schedule task [create stock history bao k hfq 4000-5000] error: {str(e)}\n{traceback.format_exc()}"
            log.error(error_msg)


if __name__ == '__main__':
    # execute_create_stock_history_bao_k_hfq_0_1000()
    # execute_create_stock_history_bao_k_hfq_1000_2000()
    # execute_create_stock_history_bao_k_hfq_2000_3000()
    # execute_create_stock_history_bao_k_hfq_3000_4000()
    execute_create_stock_history_bao_k_hfq_4000_5000()
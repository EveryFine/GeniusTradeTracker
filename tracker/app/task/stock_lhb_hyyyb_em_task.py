# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_lhb_hyyyb_em_task
   Description :
   Author :       EveryFine
   Date：          2025/6/15
-------------------------------------------------
   Change Activity:
                   2025/6/15:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

from datetime import datetime
import traceback

from sqlmodel import Session

from app.common.log import log
from app.core.db import engine
from app.crud.crud_stock_lhb_hyyyb_em import create_stock_lhb_hyyyb_em


def execute_create_stock_lhb_hyyyb_em():
    log.info(f"{datetime.now()} schedule task [create stock lhb hyyyb em(龙虎榜--每日活跃营业部--东财)）] start")
    with Session(engine) as session:
        try:
            res = create_stock_lhb_hyyyb_em(session=session)
            log.info(
                f"{datetime.now()} schedule task [create stock lhb hyyyb em(龙虎榜--每日活跃营业部--东财)）] end, res: {res}")
        except Exception as e:
            error_msg = f"{datetime.now()} schedule task [create stock lhb hyyyb em(龙虎榜--每日活跃营业部--东财)）] error: {str(e)}\n{traceback.format_exc()}"
            log.error(error_msg)


if __name__ == '__main__':
    execute_create_stock_lhb_hyyyb_em()
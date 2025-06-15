# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_lhb_yyb_detail_em_task
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
from app.crud.crud_stock_lhb_yyb_detail_em import create_stock_lhb_yyb_detail_em


def execute_create_stock_lhb_yyb_detail_em():
    log.info(f"{datetime.now()} schedule task [create stock lhb yyb detail em(龙虎榜--营业部详情数据--东财)）] start")
    with Session(engine) as session:
        try:
            create_count = create_stock_lhb_yyb_detail_em(session=session)
            log.info(
                f"{datetime.now()} schedule task [create stock lhb yyb detail em(龙虎榜--营业部详情数据--东财)）] end, create count: {create_count}")
        except Exception as e:
            error_msg = f"{datetime.now()} schedule task [create stock lhb yyb detail em(龙虎榜--营业部详情数据--东财)）] error: {str(e)}\n{traceback.format_exc()}"
            log.error(error_msg)


if __name__ == '__main__':
    execute_create_stock_lhb_yyb_detail_em()

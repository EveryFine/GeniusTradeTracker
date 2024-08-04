# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_check
   Description :
   Author :       EveryFine
   Date：          2024/8/4
-------------------------------------------------
   Change Activity:
                   2024/8/4:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

from fastapi import APIRouter

from app.api.deps import SessionDep
from app.task.stock_current_day_check_task import execute_stock_current_day_check, \
    execute_stock_history_current_day_check

router = APIRouter()


@router.post("/current", response_model=int)
def check_current_day(session: SessionDep):
    execute_stock_current_day_check()
    return 1


@router.post("/current_hist", response_model=int)
def check_current_day_hist(session: SessionDep):
    execute_stock_history_current_day_check()
    return 1

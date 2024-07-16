# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_change_abnormal
   Description :
   Author :       EveryFine
   Date：          2024/7/16
-------------------------------------------------
   Change Activity:
                   2024/7/16:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

from fastapi import APIRouter

from app.api.deps import SessionDep
from app.crud.crud_stock_change_abnormal import create_stock_change_abnormal

router = APIRouter()


@router.post("/", response_model=int)
def create_stock_change_abnormal_events(session: SessionDep):
    create_count = create_stock_change_abnormal(session=session)
    return create_count

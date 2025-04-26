# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     crud_stock_rank_lxxd
   Description :  技术指标 -- 连续下跌
   Author :       EveryFine
   Date：          2024/7/21
-------------------------------------------------
   Change Activity:
                   2024/7/21:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

from fastapi import APIRouter, HTTPException
import traceback

from app.api.deps import SessionDep
from app.crud.crud_stock_rank_lxxd import create_stock_rank_lxxd

router = APIRouter()


@router.post("/", response_model=int)
def create_all_stock_rank_lxxd(session: SessionDep):
    try:
        create_count = create_stock_rank_lxxd(session=session)
        return create_count
    except Exception as e:
        error_msg = f"Error creating stock rank lxxd: {str(e)}\n{traceback.format_exc()}"
        raise HTTPException(status_code=500, detail=error_msg)
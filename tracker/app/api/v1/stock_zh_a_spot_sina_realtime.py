# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_zh_a_spot_sina_realtime
   Description :
   Author :       EveryFine
   Date：          2025/11/25
-------------------------------------------------
   Change Activity:
                   2025/11/25:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

from fastapi import APIRouter, HTTPException
import traceback

from app.api.deps import SessionDep
from app.crud.crud_stock_zh_a_spot_sina_realtime import create_stock_zh_a_spot_sina_realtime

router = APIRouter()


@router.post("/", response_model=int)
def create_all_stock_zh_a_spot_sina_realtime(session: SessionDep):
    try:
        create_count = create_stock_zh_a_spot_sina_realtime(session=session)
        return create_count
    except Exception as e:
        error_msg = f"Error creating stock zh a spot sina realtime: {str(e)}\n{traceback.format_exc()}"
        raise HTTPException(status_code=500, detail=error_msg)
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_pool_zb
   Description :  股池--炸板
   Author :       EveryFine
   Date：          2024/7/28
-------------------------------------------------
   Change Activity:
                   2024/7/28:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

from fastapi import APIRouter, HTTPException
import traceback

from app.api.deps import SessionDep
from app.crud.crud_stock_pool_zb import create_stock_pool_zb

router = APIRouter()


@router.post("/", response_model=int)
def create_all_stock_pool_zb(session: SessionDep):
    try:
        create_count = create_stock_pool_zb(session=session)
        return create_count
    except Exception as e:
        error_msg = f"Error creating stock pool zb: {str(e)}\n{traceback.format_exc()}"
        raise HTTPException(status_code=500, detail=error_msg)

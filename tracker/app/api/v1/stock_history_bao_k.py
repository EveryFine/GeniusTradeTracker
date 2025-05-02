# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_history_bao_k
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

from fastapi import APIRouter, Query, HTTPException
import traceback

from app.api.deps import SessionDep
from app.crud.crud_stock_history_bao_k import create_stock_history_bao_k, create_part_stock_bao_k

router = APIRouter()


@router.post("/", response_model=int)
def create_stock_history_bao_k(session: SessionDep):
    try:
        create_count = create_stock_history_bao_k(session=session)
        return create_count
    except Exception as e:
        error_msg = f"Error creating stock history bao k: {str(e)}\n{traceback.format_exc()}"
        raise HTTPException(status_code=500, detail=error_msg)


@router.post("/part", response_model=int)
def create_part_stock_history_bao_k(session: SessionDep, stock_offset: int = 0,
                         stock_limit: int = Query(default=100, le=1000)):
    try:
        create_count = create_part_stock_bao_k(session=session, stock_offset=stock_offset, stock_limit=stock_limit)
        return create_count
    except Exception as e:
        error_msg = f"Error creating part stock history bao k: {str(e)}\n{traceback.format_exc()}"
        raise HTTPException(status_code=500, detail=error_msg)

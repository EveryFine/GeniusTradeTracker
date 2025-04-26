# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_rank_cxg
   Description :
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
from app.crud.crud_stock_rank_cxg import create_stock_rank_cxg

router = APIRouter()


@router.post("/", response_model=int)
def create_all_stock_rank_cxg(session: SessionDep):
    try:
        create_count = create_stock_rank_cxg(session=session)
        return create_count
    except Exception as e:
        error_msg = f"Error creating stock rank cxg: {str(e)}\n{traceback.format_exc()}"
        raise HTTPException(status_code=500, detail=error_msg)

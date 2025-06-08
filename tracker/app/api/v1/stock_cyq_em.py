# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_cyq_em
   Description :
   Author :       EveryFine
   Date：          2025/6/8
-------------------------------------------------
   Change Activity:
                   2025/6/8:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'


from fastapi import APIRouter, Query, HTTPException
import traceback

from app.api.deps import SessionDep
from app.crud.crud_stock_cyq_em import create_stock_cyq_em, create_part_stock_cyq_em

router = APIRouter()


@router.post("/", response_model=int)
def create_all_stock_cyq_em(session: SessionDep):
    try:
        create_count = create_stock_cyq_em(session=session)
        return create_count
    except Exception as e:
        error_msg = f"Error creating all stock cyq em(筹码分布): {str(e)}\n{traceback.format_exc()}"
        raise HTTPException(status_code=500, detail=error_msg)


@router.post("/part", response_model=int)
def create_part_of_stock_cyq_em(session: SessionDep, stock_offset: int = 0,
                              stock_limit: int = Query(default=100, le=1000)):
    try:
        create_count = create_part_stock_cyq_em(session=session, stock_offset=stock_offset, stock_limit=stock_limit)
        return create_count
    except Exception as e:
        error_msg = f"Error creating part stock cyq em(筹码分布): {str(e)}\n{traceback.format_exc()}"
        raise HTTPException(status_code=500, detail=error_msg)
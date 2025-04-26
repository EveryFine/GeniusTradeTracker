# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_fund_industry_rank
   Description :
   Author :       EveryFine
   Date：          2024/7/27
-------------------------------------------------
   Change Activity:
                   2024/7/27:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

from fastapi import APIRouter, HTTPException
import traceback

from app.api.deps import SessionDep
from app.crud.crud_stock_fund_industry_rank import create_stock_fund_industry_ranks

router = APIRouter()


@router.post("/", response_model=int)
def create_all_stock_fund_industry_rank(session: SessionDep):
    try:
        create_count = create_stock_fund_industry_ranks(session=session)
        return create_count
    except Exception as e:
        error_msg = f"Error creating stock fund industry ranks: {str(e)}\n{traceback.format_exc()}"
        raise HTTPException(status_code=500, detail=error_msg)
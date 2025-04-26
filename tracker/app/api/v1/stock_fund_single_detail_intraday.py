# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_fund_single_detail_intraday
   Description :  资金流 -- 个股 -- 详细 -- 即时
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
from app.crud.crud_stock_fund_single_detail_intraday import create_stock_fund_single_detail_intraday

router = APIRouter()


@router.post("/", response_model=int)
def create_all_stock_fund_single_detail_intraday(session: SessionDep):
    try:
        create_count = create_stock_fund_single_detail_intraday(session=session)
        return create_count
    except Exception as e:
        error_msg = f"Error creating stock fund single detail intraday: {str(e)}\n{traceback.format_exc()}"
        raise HTTPException(status_code=500, detail=error_msg)

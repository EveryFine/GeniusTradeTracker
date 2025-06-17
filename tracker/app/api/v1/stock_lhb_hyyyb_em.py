# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_lhb_hyyyb_em
   Description :
   Author :       EveryFine
   Date：          2025/6/15
-------------------------------------------------
   Change Activity:
                   2025/6/15:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

from fastapi import APIRouter, HTTPException
import traceback

from pydantic import BaseModel

from app.api.deps import SessionDep
from app.crud.crud_stock_lhb_hyyyb_em import create_stock_lhb_hyyyb_em

router = APIRouter()


class CreateResult(BaseModel):
    start_date: str
    end_date: str
    count: int


@router.post("/", response_model=CreateResult)
def create_all_stock_lhb_hyyyb_em(session: SessionDep):
    try:
        res = create_stock_lhb_hyyyb_em(session=session)
        return res
    except Exception as e:
        error_msg = f"Error creating stock lhb hyyyb em: {str(e)}\n{traceback.format_exc()}"
        raise HTTPException(status_code=500, detail=error_msg)

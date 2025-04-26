# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_info
   Description :
   Author :       EveryFine
   Date：          2024/7/3
-------------------------------------------------
   Change Activity:
                   2024/7/3:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

from typing import List

from fastapi import APIRouter, Query, HTTPException
import traceback

from app.api.deps import SessionDep
from app.crud.crud_stock_info import create_stock_infos, get_stock_infos
from app.models.stock_info import StockInfosPublic, StockInfo

router = APIRouter()


@router.get("/", response_model=StockInfosPublic)
def read_artists(session: SessionDep,
                 offset: int = 0,
                 limit: int = Query(default=100, le=100)):
    try:
        exchanges = get_stock_infos(session=session, offset=offset, limit=limit)
        return exchanges
    except Exception as e:
        error_msg = f"Error reading stock infos: {str(e)}\n{traceback.format_exc()}"
        raise HTTPException(status_code=500, detail=error_msg)


@router.post("/", response_model=List[StockInfo])
def create_stock_exchange(session: SessionDep):
    try:
        stock_exchanges = create_stock_infos(session=session)
        return stock_exchanges
    except Exception as e:
        error_msg = f"Error creating stock infos: {str(e)}\n{traceback.format_exc()}"
        raise HTTPException(status_code=500, detail=error_msg)

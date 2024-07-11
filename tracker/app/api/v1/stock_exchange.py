# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_exchange
   Description : 获取或更新交易所信息
                1. 创建交易所信息列表（数据后台自动获取，不从接口传入）
                2. 更新交易所股票数量信息（数据后台自动获取，不从接口传入）
                3. 读取交易所信息列表
   Author :       EveryFine
   Date：          2024/6/30
-------------------------------------------------
   Change Activity:
                   2024/6/30:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

from typing import List

from fastapi import APIRouter, Query

from app.api.deps import SessionDep
from app.crud.crud_stock_exchange import create_stock_exchanges, get_stock_exchanges
from app.models.stock_exchange import StockExchange, StockExchangesPublic

router = APIRouter()


@router.get("/", response_model=StockExchangesPublic)
def read_artists(session: SessionDep,
                 offset: int = 0,
                 limit: int = Query(default=100, le=100)):
    exchanges = get_stock_exchanges(session=session, offset=offset, limit=limit)

    return exchanges


@router.post("/", response_model=List[StockExchange])
def create_stock_exchange(session: SessionDep):
    stock_exchanges = create_stock_exchanges(session=session)
    return stock_exchanges

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

from fastapi import APIRouter

from app.api.deps import SessionDep
from app.crud.crud_stock_exchange import create_stock_exchanges
from app.models.stock_exchange import StockExchange

router = APIRouter()

@router.post("/", response_model=List[StockExchange])
def create_hero(session: SessionDep):
    stock_exchanges = create_stock_exchanges(session=session)
    return stock_exchanges
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_exchange
   Description : 证券交易所信息
   Author :       EveryFine
   Date：          2024/6/30
-------------------------------------------------
   Change Activity:
                   2024/6/30:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

from sqlmodel import SQLModel, Field


class StockExchangeBase(SQLModel):
    name: str = Field(max_length=120, description='名称')
    city: str = Field(max_length=120, description='所在城市')
    akshare_abb: str | None = Field(max_length=20, description='akshare简称')
    yfinance_abb: str | None = Field(default=None,max_length=20, description='yfinance简称')
    stock_count: int | None= Field(default=None)

class StockExchange(StockExchangeBase, table=True):
    """stock_exchange表"""
    id: int | None = Field(default=None,primary_key=True, description='id')


class StockExchangeCreate(StockExchangeBase):
    pass

class StockExchangePublic(StockExchangeBase):
    id: int

class StockExchangesPublic(SQLModel):
    data: list[StockExchangePublic]
    count: int
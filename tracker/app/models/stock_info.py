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

import datetime

from sqlmodel import SQLModel, Field


class StockInfoBase(SQLModel):
    market_value: float | None = Field(default=None, description='总市值')
    traded_market_value: float | None = Field(default=None, description='流通市值')
    industry: str | None = Field(max_length=50, description='行业')
    offering_date: datetime.date | None = Field(default=datetime.date.today(), description='上市时间')
    symbol: str = Field(max_length=20, description='股票代码')
    short_name: str | None = Field(max_length=20, description='股票简称')
    total_share_capital: float | None = Field(default=None, description='总股本')
    outstanding_shares: float | None = Field(default=None, description='流通股本')
    exchange: str | None = Field(max_length=10, description='交易所')


class StockInfo(StockInfoBase, table=True):
    """stock_info表"""
    __tablename__ = "stock_info"
    id: int | None = Field(default=None, primary_key=True, description='id')


class StockInfoCreate(StockInfoBase):
    pass


class StockInfoPublic(StockInfoBase):
    id: int


class StockInfosPublic(SQLModel):
    data: list[StockInfoPublic]
    count: int

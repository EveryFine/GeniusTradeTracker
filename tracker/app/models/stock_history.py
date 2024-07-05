# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_history
   Description :
   Author :       EveryFine
   Date：          2024/7/4
-------------------------------------------------
   Change Activity:
                   2024/7/4:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

import datetime

from sqlmodel import SQLModel, Field


class StockHistoryBase(SQLModel):
    symbol: str = Field(max_length=20, description='股票代码', index=True)
    date: datetime.date | None = Field(default=datetime.date.today(), description='日期', index=True)
    open: float | None = Field(default=None, description='开盘价')
    close: float | None = Field(default=None, description='收盘价')
    high: float | None = Field(default=None, description='最高价')
    low: float | None = Field(default=None, description='最低价')
    volume: int | None = Field(default=None, description='成交量')
    turnover: float | None = Field(default=None, description='成交额')
    range: float | None = Field(default=None, description='振幅')
    change_rate: float | None = Field(default=None, description='涨跌幅')
    change_amount: float | None = Field(default=None, description='涨跌额')
    turnover_rate: float | None = Field(default=None, description='换手率')


class StockHistory(StockHistoryBase, table=True):
    """stock_history表"""
    __tablename__ = "stock_history"
    id: int | None = Field(default=None, primary_key=True, description='id')


class StockHistoryCreate(StockHistoryBase):
    pass


class StockHistoryPublic(StockHistoryBase):
    id: int


class StockHistoriesPublic(SQLModel):
    data: list[StockHistoryPublic]
    count: int

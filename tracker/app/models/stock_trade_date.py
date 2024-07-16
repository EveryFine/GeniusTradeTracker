# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_trade_date
   Description :
   Author :       EveryFine
   Date：          2024/7/16
-------------------------------------------------
   Change Activity:
                   2024/7/16:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

import datetime

from sqlmodel import Field, SQLModel


class StockTradeDateBase(SQLModel):
    trade_date: datetime.date = Field(description='交易日期', index=True)
    created_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='创建时间', index=True)
    updated_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='更新时间', index=True)


class StockTradeDate(StockTradeDateBase, table=True):
    """stock_trade_date表"""
    __tablename__ = "stock_trade_date"
    id: int | None = Field(default=None, primary_key=True, description='id')


class StockTradeDateCreate(StockTradeDateBase):
    pass


class StockTradeDatePublic(StockTradeDateBase):
    id: int


class StockTradeDatesPublic(SQLModel):
    data: list[StockTradeDatePublic]
    count: int

# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_lhb_yyb_detail_em
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

import datetime
from sqlmodel import SQLModel, Field


class StockLhbYybDetailEmBase(SQLModel):
    yyb_symbol: str = Field(max_length=20, description='营业部代码')
    yyb_name: str | None = Field(max_length=100, description='营业部名称')
    yyb_short_name: str | None = Field(max_length=100, description='营业部简称')
    trade_date: datetime.date | None = Field(default=datetime.date.today(), description='交易日期', index=True)
    stock_symbol: str | None = Field(max_length=40, description='股票代码')
    stock_name: str | None = Field(max_length=40, description='股票名称')
    change_rate: float | None = Field(default=None, description='涨跌幅')
    buy_amount: float | None = Field(default=None, description='买入金额')
    sell_amount: float | None = Field(default=None, description='卖出金额')
    net_amount: float | None = Field(default=None, description='净额')
    reason: str | None = Field(max_length=400, description='上榜原因')

    created_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='创建时间', index=True)
    updated_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='更新时间', index=True)


class StockLhbYybDetailEm(StockLhbYybDetailEmBase, table=True):
    """stock_lhb_yyb_detail_em表"""
    __tablename__ = "stock_lhb_yyb_detail_em"
    id: int | None = Field(default=None, primary_key=True, description='id')


class StockLhbYybDetailEmCreate(StockLhbYybDetailEmBase):
    pass


class StockLhbYybDetailEmPublic(StockLhbYybDetailEmBase):
    id: int


class StockLhbYybDetailEmAllPublic(SQLModel):
    data: list[StockLhbYybDetailEmPublic]
    count: int
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_fund_big_deal
   Description :  资金流 -- 大单追踪
   Author :       EveryFine
   Date：          2024/7/27
-------------------------------------------------
   Change Activity:
                   2024/7/27:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

import datetime

from sqlmodel import SQLModel, Field


class StockFundBigDealBase(SQLModel):
    trade_date: datetime.date | None = Field(default=datetime.date.today(), description='日期', index=True)
    trade_time: datetime.datetime | None = Field(default=datetime.datetime.now(), description='成交时间', index=True)
    symbol: str = Field(max_length=20, description='股票代码', index=True)
    name: str | None = Field(max_length=40, description='股票简称')
    price: float | None = Field(default=None, description='成交价格')
    volume: int | None = Field(default=None, description='成交量')
    turnover: float | None = Field(default=None, description='成交额')
    type: str = Field(max_length=20, description='大单性质')
    change_rate: float | None = Field(default=None, description='涨跌幅')
    change_amount: float | None = Field(default=None, description='涨跌额')
    created_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='创建时间', index=True)
    updated_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='更新时间', index=True)


class StockFundBigDeal(StockFundBigDealBase, table=True):
    """stock_fund_big_deal表"""
    __tablename__ = "stock_fund_big_deal"
    id: int | None = Field(default=None, primary_key=True, description='id')


class StockFundBigDealCreate(StockFundBigDealBase):
    pass


class StockFundBigDealPublic(StockFundBigDealBase):
    id: int


class StockFundBigDealAllPublic(SQLModel):
    data: list[StockFundBigDealPublic]
    count: int
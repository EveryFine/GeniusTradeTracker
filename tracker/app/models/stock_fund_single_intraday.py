# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_fund_single_intraday
   Description :  资金流 -- 个股 -- 即时
   Author :       EveryFine
   Date：          2024/7/25
-------------------------------------------------
   Change Activity:
                   2024/7/25:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

import datetime

from sqlmodel import SQLModel, Field
class StockFundSingleIntradayBase(SQLModel):
    trade_date: datetime.date | None = Field(default=datetime.date.today(), description='日期', index=True)
    symbol: str = Field(max_length=20, description='股票代码', index=True)
    name: str | None = Field(max_length=40, description='股票名称')
    latest_price: float | None = Field(default=None, description='最新价')
    change_rate: float | None = Field(default=None, description='涨跌幅')
    turnover_rate: float | None = Field(default=None, description='换手率')
    fund_in: float | None = Field(default=None, description='流入资金')
    fund_out: float | None = Field(default=None, description='流出资金')
    net_amount: float | None = Field(default=None, description='净额')
    turnover: float | None = Field(default=None, description='成交额')
    created_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='创建时间', index=True)
    updated_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='更新时间', index=True)

class StockFundSingleIntraday(StockFundSingleIntradayBase, table=True):
    """stock_fund_single_intraday表"""
    __tablename__ = "stock_fund_single_intraday"
    id: int | None = Field(default=None, primary_key=True, description='id')


class StockFundSingleIntradayCreate(StockFundSingleIntradayBase):
    pass


class StockFundSingleIntradayPublic(StockFundSingleIntradayBase):
    id: int


class StockFundSingleIntradayAllPublic(SQLModel):
    data: list[StockFundSingleIntradayPublic]
    count: int
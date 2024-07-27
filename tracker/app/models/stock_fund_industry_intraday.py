# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_fund_industry_intraday
   Description :  资金流 -- 行业 -- 即时
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


class StockFundIndustryIntradayBase(SQLModel):
    trade_date: datetime.date | None = Field(default=datetime.date.today(), description='日期', index=True)
    name: str | None = Field(max_length=40, description='行业名称')
    index: float | None = Field(default=None, description='行业指数')
    change_rate: float | None = Field(default=None, description='行业涨跌幅')
    change_rate_rank: float | None = Field(default=None, description='行业涨跌幅排名')
    fund_in: float | None = Field(default=None, description='流入资金')
    fund_out: float | None = Field(default=None, description='流出资金')
    net_amount: float | None = Field(default=None, description='净额')
    firm_number: int | None = Field(default=None, description='公司家数')
    best_stock: str | None = Field(max_length=40, description='领涨股')
    best_change_rate: float | None = Field(default=None, description='领涨股涨跌幅')
    best_latest_price: float | None = Field(default=None, description='领涨股当前价')
    created_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='创建时间', index=True)
    updated_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='更新时间', index=True)


class StockFundIndustryIntraday(StockFundIndustryIntradayBase, table=True):
    """stock_fund_industry_intraday表"""
    __tablename__ = "stock_fund_industry_intraday"
    id: int | None = Field(default=None, primary_key=True, description='id')


class StockFundIndustryIntradayCreate(StockFundIndustryIntradayBase):
    pass


class StockFundIndustryIntradayPublic(StockFundIndustryIntradayBase):
    id: int


class StockFundIndustryIntradayAllPublic(SQLModel):
    data: list[StockFundIndustryIntradayPublic]
    count: int
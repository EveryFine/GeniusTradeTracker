# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_fund_single_rank
   Description :  资金流 -- 个股 -- 排行：3日，5日，10日，20日
   Author :       EveryFine
   Date：          2024/7/26
-------------------------------------------------
   Change Activity:
                   2024/7/26:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

import datetime

from sqlmodel import SQLModel, Field


class StockFundSingleRankBase(SQLModel):
    trade_date: datetime.date | None = Field(default=datetime.date.today(), description='日期', index=True)
    range_type: str = Field(max_length=20, description='排行类型：3日，5日，10日，20日', index=True)
    symbol: str = Field(max_length=20, description='股票代码', index=True)
    name: str | None = Field(max_length=40, description='股票名称')
    latest_price: float | None = Field(default=None, description='最新价')
    change_rate: float | None = Field(default=None, description='阶段涨跌幅')
    change_rate_rank: float | None = Field(default=None, description='阶段涨跌幅排名')
    turnover_rate: float | None = Field(default=None, description='连续换手率')
    fund_in_net: float | None = Field(default=None, description='流入资金净额')
    created_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='创建时间', index=True)
    updated_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='更新时间', index=True)


class StockFundSingleRank(StockFundSingleRankBase, table=True):
    """stock_fund_single_rank表"""
    __tablename__ = "stock_fund_single_rank"
    id: int | None = Field(default=None, primary_key=True, description='id')


class StockFundSingleRankCreate(StockFundSingleRankBase):
    pass


class StockFundSingleRankPublic(StockFundSingleRankBase):
    id: int


class StockFundSingleRankAllPublic(SQLModel):
    data: list[StockFundSingleRankPublic]
    count: int

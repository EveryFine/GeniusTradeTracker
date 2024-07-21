# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_rank_xstp
   Description :   技术指标 -- 向上突破
   Author :       EveryFine
   Date：          2024/7/21
-------------------------------------------------
   Change Activity:
                   2024/7/21:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

import datetime

from sqlmodel import SQLModel, Field


class StockRankXstpBase(SQLModel):
    trade_date: datetime.date | None = Field(default=datetime.date.today(), description='日期', index=True)
    range_type: str = Field(max_length=20, description='突破类型', index=True)  # {"5日均线", "10日均线", "20日均线", "30日均线", "60日均线", "90日均线", "250日均线", "500日均线"}
    symbol: str = Field(max_length=20, description='股票代码', index=True)
    name: str | None = Field(max_length=40, description='股票简称')
    latest_price: float | None = Field(default=None, description='最新价')
    turnover: float | None = Field(default=None, description='成交额')
    volume: int | None = Field(default=None, description='成交量')
    change_rate: float | None = Field(default=None, description='涨跌幅')
    turnover_rate: float | None = Field(default=None, description='换手率')

    created_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='创建时间', index=True)
    updated_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='更新时间', index=True)


class StockRankXstp(StockRankXstpBase, table=True):
    """stock_rank_xstp表"""
    __tablename__ = "stock_rank_xstp"
    id: int | None = Field(default=None, primary_key=True, description='id')


class StockRankXstpCreate(StockRankXstpBase):
    pass


class StockRankXstpPublic(StockRankXstpBase):
    id: int


class StockRankXstpAllPublic(SQLModel):
    data: list[StockRankXstpPublic]
    count: int
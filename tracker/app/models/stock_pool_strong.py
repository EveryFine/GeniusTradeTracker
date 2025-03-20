# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_pool_strong
   Description :   股池--强势
   Author :       EveryFine
   Date：          2024/7/28
-------------------------------------------------
   Change Activity:
                   2024/7/28:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

import datetime

from sqlmodel import SQLModel, Field


class StockPoolStrongBase(SQLModel):
    trade_date: datetime.date | None = Field(default=datetime.date.today(), description='日期', index=True)
    symbol: str = Field(max_length=20, description='股票代码', index=True)
    name: str | None = Field(max_length=40, description='股票名称')
    change_rate: float | None = Field(default=None, description='涨跌幅')
    latest_price: float | None = Field(default=None, description='最新价')

    zt_price: float | None = Field(default=None, description='涨停价')
    turnover: float | None = Field(default=None, description='成交额')
    traded_market_value: float | None = Field(default=None, description='流通市值')
    market_value: float | None = Field(default=None, description='总市值')
    turnover_rate: float | None = Field(default=None, description='换手率')
    up_speed: float | None = Field(default=None, description='涨速')
    is_new_high: str | None = Field(default=False, description='是否新高')
    volume_ratio: float | None = Field(default=None, description='量比')
    zt_status: str | None = Field(max_length=20, description='涨停统计')

    reason: str | None = Field(default=None,
                               description='入选理由：1: 60日新高, 2: 近期多次涨停, 3: 60日新高且近期多次涨停')
    industry: str | None = Field(max_length=50, description='所属行业')

    created_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='创建时间', index=True)
    updated_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='更新时间', index=True)


class StockPoolStrong(StockPoolStrongBase, table=True):
    """stock_pool_strong表"""
    __tablename__ = "stock_pool_strong"
    id: int | None = Field(default=None, primary_key=True, description='id')


class StockPoolStrongCreate(StockPoolStrongBase):
    pass


class StockPoolStrongPublic(StockPoolStrongBase):
    id: int


class StockPoolStrongAllPublic(SQLModel):
    data: list[StockPoolStrongPublic]
    count: int

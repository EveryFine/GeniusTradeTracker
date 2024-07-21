# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_rank_cxd
   Description :   技术指标 -- 创新低
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


class StockRankCxdBase(SQLModel):
    trade_date: datetime.date | None = Field(default=datetime.date.today(), description='日期', index=True)
    range_type: str = Field(max_length=20, description='新低类型', index=True)  # {"创月新低", "半年新低", "一年新低", "历史新低"}
    symbol: str = Field(max_length=20, description='股票代码', index=True)
    name: str | None = Field(max_length=40, description='股票名称')
    change_rate: float | None = Field(default=None, description='涨跌幅')
    turnover_rate: float | None = Field(default=None, description='换手率')
    latest_price: float | None = Field(default=None, description='最新价')
    pre_low: float | None = Field(default=None, description='前期低点')
    pre_low_date: datetime.date | None = Field(default=None, description='前期低点日期')
    created_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='创建时间', index=True)
    updated_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='更新时间', index=True)


class StockRankCxd(StockRankCxdBase, table=True):
    """stock_rank_cxd表"""
    __tablename__ = "stock_rank_cxd"
    id: int | None = Field(default=None, primary_key=True, description='id')


class StockRankCxdCreate(StockRankCxdBase):
    pass


class StockRankCxdPublic(StockRankCxdBase):
    id: int


class StockRankCxdAllPublic(SQLModel):
    data: list[StockRankCxdPublic]
    count: int

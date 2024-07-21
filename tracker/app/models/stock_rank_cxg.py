# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_rank_cxg
   Description : 技术指标 -- 创新高
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


class StockRankCxgBase(SQLModel):
    trade_date: datetime.date | None = Field(default=datetime.date.today(), description='日期', index=True)
    range_type: str = Field(max_length=20, description='新高类型', index=True)  # {"创月新高", "半年新高", "一年新高", "历史新高"}
    symbol: str = Field(max_length=20, description='股票代码', index=True)
    name: str | None = Field(max_length=40, description='股票名称')
    change_rate: float | None = Field(default=None, description='涨跌幅')
    turnover_rate: float | None = Field(default=None, description='换手率')
    latest_price: float | None = Field(default=None, description='最新价')
    pre_high: float | None = Field(default=None, description='前期高点')
    pre_high_date: datetime.date | None = Field(default=None, description='前期高点日期')
    created_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='创建时间', index=True)
    updated_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='更新时间', index=True)


class StockRankCxg(StockRankCxgBase, table=True):
    """stock_rank_cxg表"""
    __tablename__ = "stock_rank_cxg"
    id: int | None = Field(default=None, primary_key=True, description='id')


class StockRankCxgCreate(StockRankCxgBase):
    pass


class StockRankCxgPublic(StockRankCxgBase):
    id: int


class StockRankCxgAllPublic(SQLModel):
    data: list[StockRankCxgPublic]
    count: int

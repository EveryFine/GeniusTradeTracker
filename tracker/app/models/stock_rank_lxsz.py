# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_rank_lxsz
   Description :  技术指标 -- 连续上涨
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


class StockRankLxszBase(SQLModel):
    trade_date: datetime.date | None = Field(default=datetime.date.today(), description='日期', index=True)
    symbol: str = Field(max_length=20, description='股票代码', index=True)
    name: str | None = Field(max_length=40, description='股票名称')
    close: float | None = Field(default=None, description='收盘价')
    high: float | None = Field(default=None, description='最高价')
    low: float | None = Field(default=None, description='最低价')
    lz_days: int | None = Field(default=None, description='连涨天数')
    lz_change_rate: float | None = Field(default=None, description='连续涨跌幅')
    turnover_rate: float | None = Field(default=None, description='累计换手率')
    industry: str | None = Field(max_length=50, description='所属行业')
    created_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='创建时间', index=True)
    updated_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='更新时间', index=True)


class StockRankLxsz(StockRankLxszBase, table=True):
    """stock_rank_lxsz表"""
    __tablename__ = "stock_rank_lxsz"
    id: int | None = Field(default=None, primary_key=True, description='id')


class StockRankLxszCreate(StockRankLxszBase):
    pass


class StockRankLxszPublic(StockRankLxszBase):
    id: int


class StockRankLxszAllPublic(SQLModel):
    data: list[StockRankLxszPublic]
    count: int

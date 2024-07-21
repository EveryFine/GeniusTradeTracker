# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_rank_cxfl
   Description :   技术指标 -- 持续放量
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


class StockRankCxflBase(SQLModel):
    trade_date: datetime.date | None = Field(default=datetime.date.today(), description='日期', index=True)
    symbol: str = Field(max_length=20, description='股票代码', index=True)
    name: str | None = Field(max_length=40, description='股票名称')
    change_rate: float | None = Field(default=None, description='涨跌幅')
    latest_price: float | None = Field(default=None, description='最新价')
    base_date: datetime.date | None = Field(default=datetime.date.today(), description='基准日')
    fl_days: int | None = Field(default=None, description='放量天数')
    days_change_rate: float | None = Field(default=None, description='阶段涨跌幅')
    industry: str | None = Field(max_length=50, description='所属行业')
    created_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='创建时间', index=True)
    updated_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='更新时间', index=True)


class StockRankCxfl(StockRankCxflBase, table=True):
    """stock_rank_cxfl表"""
    __tablename__ = "stock_rank_cxfl"
    id: int | None = Field(default=None, primary_key=True, description='id')


class StockRankCxflCreate(StockRankCxflBase):
    pass


class StockRankCxflPublic(StockRankCxflBase):
    id: int


class StockRankCxflAllPublic(SQLModel):
    data: list[StockRankCxflPublic]
    count: int
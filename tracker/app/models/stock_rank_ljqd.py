# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_rank_ljqd
   Description :    技术指标 -- 量价齐跌
   Author :       EveryFine
   Date：          2024/7/22
-------------------------------------------------
   Change Activity:
                   2024/7/22:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

import datetime

from sqlmodel import SQLModel, Field


class StockRankLjqdBase(SQLModel):
    trade_date: datetime.date | None = Field(default=datetime.date.today(), description='日期', index=True)
    symbol: str = Field(max_length=20, description='股票代码', index=True)
    name: str | None = Field(max_length=40, description='股票名称')
    latest_price: float | None = Field(default=None, description='最新价')
    qd_days: int | None = Field(default=None, description='量价齐跌天数')
    days_change_rate: float | None = Field(default=None, description='阶段涨幅')
    turnover_rate: float | None = Field(default=None, description='累计换手率')
    industry: str | None = Field(max_length=50, description='所属行业')
    created_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='创建时间', index=True)
    updated_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='更新时间', index=True)


class StockRankLjqd(StockRankLjqdBase, table=True):
    """stock_rank_ljqd表"""
    __tablename__ = "stock_rank_ljqd"
    id: int | None = Field(default=None, primary_key=True, description='id')


class StockRankLjqdCreate(StockRankLjqdBase):
    pass


class StockRankLjqdPublic(StockRankLjqdBase):
    id: int


class StockRankLjqdAllPublic(SQLModel):
    data: list[StockRankLjqdPublic]
    count: int
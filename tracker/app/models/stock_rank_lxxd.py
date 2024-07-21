# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_rank_lxxd
   Description :   技术指标 -- 连续下跌
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


class StockRankLxxdBase(SQLModel):
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


class StockRankLxxd(StockRankLxxdBase, table=True):
    """stock_rank_lxxd表"""
    __tablename__ = "stock_rank_lxxd"
    id: int | None = Field(default=None, primary_key=True, description='id')


class StockRankLxxdCreate(StockRankLxxdBase):
    pass


class StockRankLxxdPublic(StockRankLxxdBase):
    id: int


class StockRankLxxdAllPublic(SQLModel):
    data: list[StockRankLxxdPublic]
    count: int
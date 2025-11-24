# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_market_activity_realtime
   Description :
   Author :       EveryFine
   Date：          2025/11/24
-------------------------------------------------
   Change Activity:
                   2025/11/24:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

import datetime

from sqlmodel import SQLModel, Field


class StockMarketActivityRealtimeBase(SQLModel):
    trade_date: datetime.date | None = Field(default=datetime.date.today(), description='日期', index=True)
    collect_time: datetime.datetime | None = Field(default_factory=lambda: datetime.datetime.now(),
                                                   description='时间', index=True)

    advancing: int | None = Field(default=None, description='上涨家数')
    limit_up: int | None = Field(default=None, description='涨停')
    true_limit_up: int | None = Field(default=None, description='真实涨停')
    st_limit_up: int | None = Field(default=None, description='st st*涨停')
    declining: int | None = Field(default=None, description='下跌')
    limit_down: int | None = Field(default=None, description='跌停')
    true_limit_down: int | None = Field(default=None, description='真实跌停')
    st_limit_down: int | None = Field(default=None, description='st st*跌停')
    unchanged: int | None = Field(default=None, description='平盘')
    suspended: int | None = Field(default=None, description='停牌')
    activity_rate: float | None = Field(default=None, description='活跃度，百分比')
    statistical_date: datetime.datetime | None = Field(default_factory=lambda: datetime.datetime.now(),
                                                       description='统计日期')

    created_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='创建时间', index=True)
    updated_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='更新时间', index=True)


class StockMarketActivityRealtime(StockMarketActivityRealtimeBase, table=True):
    """stock_market_activity_realtime表"""
    __tablename__ = "stock_market_activity_realtime"
    id: int | None = Field(default=None, primary_key=True, description='id')


class StockMarketActivityRealtimeCreate(StockMarketActivityRealtimeBase):
    pass


class StockMarketActivityRealtimePublic(StockMarketActivityRealtimeBase):
    id: int


class StockMarketActivityRealtimeAllPublic(SQLModel):
    data: list[StockMarketActivityRealtimePublic]
    count: int

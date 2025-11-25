# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_zh_a_spot_sina_realtime
   Description :
   Author :       EveryFine
   Date：          2025/11/25
-------------------------------------------------
   Change Activity:
                   2025/11/25:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

import datetime

from sqlmodel import SQLModel, Field


class StockZhASpotSinaRealtimeBase(SQLModel):
    trade_date: datetime.date | None = Field(default=datetime.date.today(), description='日期', index=True)
    collect_time: datetime.datetime | None = Field(default_factory=lambda: datetime.datetime.now(),
                                                   description='时间', index=True)
    code: str = Field(max_length=20, description='股票代码，带市场标识', index=True)
    symbol: str = Field(max_length=20, description='股票代码，不带市场标识', index=True)
    name: str | None = Field(max_length=40, description='名称')
    latest_price: float | None = Field(default=None, description='最新价')
    change_amount: float | None = Field(default=None, description='涨跌额')
    change_rate: float | None = Field(default=None, description='涨跌幅')
    buy_in: float | None = Field(default=None, description='买入')
    sell_out: float | None = Field(default=None, description='卖出')
    pre_close: float | None = Field(default=None, description='昨收')
    open: float | None = Field(default=None, description='今开')
    high: float | None = Field(default=None, description='最高')
    low: float | None = Field(default=None, description='最低')
    volume: int | None = Field(default=None, description='成交量')
    turnover: float | None = Field(default=None, description='成交额')

    data_timestamp: datetime.time | None = Field(default=None,
                                                 description='时间戳')
    created_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='创建时间', index=True)
    updated_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='更新时间', index=True)


class StockZhASpotSinaRealtime(StockZhASpotSinaRealtimeBase, table=True):
    """stock_zh_a_spot_sina_realtime表"""
    __tablename__ = "stock_zh_a_spot_sina_realtime"
    id: int | None = Field(default=None, primary_key=True, description='id')


class StockZhASpotSinaRealtimeCreate(StockZhASpotSinaRealtimeBase):
    pass


class StockZhASpotSinaRealtimePublic(StockZhASpotSinaRealtimeBase):
    id: int


class StockZhASpotSinaRealtimeAllPublic(SQLModel):
    data: list[StockZhASpotSinaRealtimePublic]
    count: int

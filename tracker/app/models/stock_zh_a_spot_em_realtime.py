# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_zh_a_spot_em_realtime
   Description :
   Author :       EveryFine
   Date：          2025/6/29
-------------------------------------------------
   Change Activity:
                   2025/6/29:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

import datetime

from sqlmodel import SQLModel, Field


class StockZhASpotEmRealtimeBase(SQLModel):
    trade_date: datetime.date | None = Field(default=datetime.date.today(), description='日期', index=True)
    collect_time: datetime.time | None = Field(default_factory=lambda: datetime.datetime.now().time(),
                                               description='时间', index=True)
    symbol: str = Field(max_length=20, description='代码', index=True)
    name: str | None = Field(max_length=40, description='名称')
    latest_price: float | None = Field(default=None, description='最新价')
    change_rate: float | None = Field(default=None, description='涨跌幅')

    change_amount: float | None = Field(default=None, description='涨跌额')
    volume: int | None = Field(default=None, description='成交量')
    turnover: float | None = Field(default=None, description='成交额')

    range: float | None = Field(default=None, description='振幅')

    high: float | None = Field(default=None, description='最高')
    low: float | None = Field(default=None, description='最低')
    open: float | None = Field(default=None, description='今开')
    pre_close: float | None = Field(default=None, description='昨收')

    volume_ratio: float | None = Field(default=None, description='量比')
    turnover_rate: float | None = Field(default=None, description='换手率')

    forward_pe_ratio: float | None = Field(default=None, description='市盈率-动态')
    pb_mrq: float | None = Field(default=None, description='市净率')

    market_value: float | None = Field(default=None, description='总市值')
    traded_market_value: float | None = Field(default=None, description='流通市值')

    up_speed: float | None = Field(default=None, description='涨速')

    change_rate_5min: float | None = Field(default=None, description='5分钟涨跌')
    change_rate_60d: float | None = Field(default=None, description='60日涨跌幅')
    change_rate_ytd: float | None = Field(default=None, description='年初至今涨跌幅')

    created_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='创建时间', index=True)
    updated_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='更新时间', index=True)


class StockZhASpotEmRealtime(StockZhASpotEmRealtimeBase, table=True):
    """stock_zh_a_spot_em_realtime表"""
    __tablename__ = "stock_zh_a_spot_em_realtime"
    id: int | None = Field(default=None, primary_key=True, description='id')


class StockZhASpotEmRealtimeCreate(StockZhASpotEmRealtimeBase):
    pass


class StockZhASpotEmRealtimePublic(StockZhASpotEmRealtimeBase):
    id: int


class StockZhASpotEmRealtimeAllPublic(SQLModel):
    data: list[StockZhASpotEmRealtimePublic]
    count: int
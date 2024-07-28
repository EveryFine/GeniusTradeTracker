# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_pool_dt
   Description :  股池--跌停
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


class StockPoolDtBase(SQLModel):
    trade_date: datetime.date | None = Field(default=datetime.date.today(), description='日期', index=True)
    symbol: str = Field(max_length=20, description='股票代码', index=True)
    name: str | None = Field(max_length=40, description='股票名称')
    change_rate: float | None = Field(default=None, description='涨跌幅')
    latest_price: float | None = Field(default=None, description='最新价')

    turnover: float | None = Field(default=None, description='成交额')
    traded_market_value: float | None = Field(default=None, description='流通市值')
    market_value: float | None = Field(default=None, description='总市值')

    forward_pe_ratio: float | None = Field(default=None, description='动态市盈率')

    turnover_rate: float | None = Field(default=None, description='换手率')
    fd_fund: float | None = Field(default=None, description='封单资金')
    fb_last_time: datetime.time | None = Field(default=None, description='最后封板时间')
    bs_turnover: float | None = Field(default=None, description='板上成交额')
    lb_count: int | None = Field(default=None, description='连续跌停')
    kb_count: int | None = Field(default=None, description='开板次数')

    industry: str | None = Field(max_length=50, description='所属行业')

    created_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='创建时间', index=True)
    updated_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='更新时间', index=True)


class StockPoolDt(StockPoolDtBase, table=True):
    """stock_pool_dt表"""
    __tablename__ = "stock_pool_dt"
    id: int | None = Field(default=None, primary_key=True, description='id')


class StockPoolDtCreate(StockPoolDtBase):
    pass


class StockPoolDtPublic(StockPoolDtBase):
    id: int


class StockPoolDtAllPublic(SQLModel):
    data: list[StockPoolDtPublic]
    count: int
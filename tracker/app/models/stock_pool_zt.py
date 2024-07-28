# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_pool_zt
   Description : 股池--涨停
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


class StockPoolZtBase(SQLModel):
    trade_date: datetime.date | None = Field(default=datetime.date.today(), description='日期', index=True)
    symbol: str = Field(max_length=20, description='股票代码', index=True)
    name: str | None = Field(max_length=40, description='股票名称')
    change_rate: float | None = Field(default=None, description='涨跌幅')
    latest_price: float | None = Field(default=None, description='最新价')

    # zt_price: float | None = Field(default=None, description='涨停价')
    turnover: float | None = Field(default=None, description='成交额')
    traded_market_value: float | None = Field(default=None, description='流通市值')
    market_value: float | None = Field(default=None, description='总市值')
    turnover_rate: float | None = Field(default=None, description='换手率')
    fb_fund: float | None = Field(default=None, description='封板资金')
    fb_first_time: datetime.time | None = Field(default=None, description='首次封板时间')
    fb_last_time: datetime.time | None = Field(default=None, description='最后封板时间')
    zb_count: int | None = Field(default=None, description='炸板次数')
    zt_status: str | None = Field(max_length=20, description='涨停统计')
    lb_count: int | None = Field(default=None, description='连板数')
    industry: str | None = Field(max_length=50, description='所属行业')
    # up_speed: float | None = Field(default=None, description='涨速')
    # range: float | None = Field(default=None, description='振幅')
    # is_new_high: bool | None = Field(default=False, description='是否新高')
    #
    # volume_ratio: float | None = Field(default=None, description='量比')

    created_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='创建时间', index=True)
    updated_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='更新时间', index=True)


class StockPoolZt(StockPoolZtBase, table=True):
    """stock_pool_zt表"""
    __tablename__ = "stock_pool_zt"
    id: int | None = Field(default=None, primary_key=True, description='id')


class StockPoolZtCreate(StockPoolZtBase):
    pass


class StockPoolZtPublic(StockPoolZtBase):
    id: int


class StockPoolZtAllPublic(SQLModel):
    data: list[StockPoolZtPublic]
    count: int
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_rank_xzjp
   Description :    技术指标 -- 险资举牌
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


class StockRankXzjpBase(SQLModel):
    pub_date: datetime.date | None = Field(default=datetime.date.today(), description='举牌公告日', index=True)
    symbol: str = Field(max_length=20, description='股票代码', index=True)
    name: str | None = Field(max_length=40, description='股票名称')
    current_price: float | None = Field(default=None, description='现价')
    change_rate: float | None = Field(default=None, description='涨跌幅')
    pub_owner: str = Field(max_length=200, description='举牌方')
    increase_amount: str = Field(max_length=20, description='增持数量')
    increase_amount_per: float | None = Field(default=None, description='增持数量占总股本比例')
    total_amount: str = Field(max_length=20, description='变动后持股总数')
    total_amount_per: float | None = Field(default=None, description='变动后持股比例')

    created_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='创建时间', index=True)
    updated_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='更新时间', index=True)


class StockRankXzjp(StockRankXzjpBase, table=True):
    """stock_rank_xzjp表"""
    __tablename__ = "stock_rank_xzjp"
    id: int | None = Field(default=None, primary_key=True, description='id')


class StockRankXzjpCreate(StockRankXzjpBase):
    pass


class StockRankXzjpPublic(StockRankXzjpBase):
    id: int


class StockRankXzjpAllPublic(SQLModel):
    data: list[StockRankXzjpPublic]
    count: int
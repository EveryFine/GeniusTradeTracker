# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_lhb_detail_em
   Description :
   Author :       EveryFine
   Date：          2025/6/15
-------------------------------------------------
   Change Activity:
                   2025/6/15:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

import datetime
from sqlmodel import SQLModel, Field


class StockLhbDetailEmBase(SQLModel):
    trade_date: datetime.date | None = Field(default=datetime.date.today(), description='上榜日', index=True)

    name: str | None = Field(max_length=40, description='名称')
    symbol: str | None = Field(max_length=20, description='股票代码')
    insight: str | None = Field(max_length=300, description='解读', index=True)
    close: float | None = Field(default=None, description='收盘价')
    change_rate: float | None = Field(default=None, description='涨跌幅')

    lhb_in_net: float | None = Field(default=None, description='龙虎榜净买额')
    lhb_in_amount: float | None = Field(default=None, description='龙虎榜买入额')
    lhb_out_amount: float | None = Field(default=None, description='龙虎榜卖出额')
    lhb_amount: float | None = Field(default=None, description='龙虎榜成交额')
    total_amount: float | None = Field(default=None, description='市场总成交额')
    in_net_per: float | None = Field(default=None, description='净买额占总成交比')
    in_amount_per: float | None = Field(default=None, description='买入额占总成交比')
    turnover_rate: float | None = Field(default=None, description='换手率')
    traded_market_value: float | None = Field(default=None, description='流通市值')
    reason: str | None = Field(max_length=400, description='上榜原因')

    created_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='创建时间', index=True)
    updated_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='更新时间', index=True)


class StockLhbDetailEm(StockLhbDetailEmBase, table=True):
    """stock_lhb_detail_em表"""
    __tablename__ = "stock_lhb_detail_em"
    id: int | None = Field(default=None, primary_key=True, description='id')


class StockLhbDetailEmCreate(StockLhbDetailEmBase):
    pass


class StockLhbDetailEmPublic(StockLhbDetailEmBase):
    id: int


class StockLhbDetailEmAllPublic(SQLModel):
    data: list[StockLhbDetailEmPublic]
    count: int
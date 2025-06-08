# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_cyq_em
   Description : 筹码分布
    接口: stock_cyq_em
    目标地址: https://quote.eastmoney.com/concept/sz000001.html
    描述: 东方财富网-概念板-行情中心-日K-筹码分布
    限量: 单次返回指定 symbol 和 adjust 的近 90 个交易日数据
   Author :       EveryFine
   Date：          2025/6/8
-------------------------------------------------
   Change Activity:
                   2025/6/8:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

import datetime

from sqlmodel import SQLModel, Field


class StockCyqEmBase(SQLModel):
    trade_date: datetime.date | None = Field(default=datetime.date.today(), description='日期', index=True)
    symbol: str = Field(max_length=20, description='股票代码', index=True)
    name: str | None = Field(max_length=40, description='股票名称')
    profit_ratio: float | None = Field(default=None, description='获利比例')
    avg_cost: float | None = Field(default=None, description='平均成本')
    cost_90_low: float | None = Field(default=None, description='90成本-低')
    cost_90_high: float | None = Field(default=None, description='90成本-高')
    concentration_90: float | None = Field(default=None, description='90集中度')
    cost_70_low: float | None = Field(default=None, description='70成本-低')
    cost_70_high: float | None = Field(default=None, description='70成本-高')
    concentration_70: float | None = Field(default=None, description=' 70集中度')

    created_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='创建时间', index=True)
    updated_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='更新时间', index=True)


class StockCyqEm(StockCyqEmBase, table=True):
    """stock_cyq_em表"""
    __tablename__ = "stock_cyq_em"
    id: int | None = Field(default=None, primary_key=True, description='id')


class StockCyqEmCreate(StockCyqEmBase):
    pass


class StockCyqEmPublic(StockCyqEmBase):
    id: int


class StockCyqEmAllPublic(SQLModel):
    data: list[StockCyqEmPublic]
    count: int
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_lhb_hyyyb_em
   Description : 每日活跃营业部
                 接口: stock_lhb_hyyyb_em
                目标地址: https://data.eastmoney.com/stock/hyyyb.html
                描述: 东方财富网-数据中心-龙虎榜单-每日活跃营业部
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


class StockLhbHyyybEmBase(SQLModel):
    yyb_symbol: str = Field(max_length=20, description='营业部代码')
    yyb_name: str | None = Field(max_length=40, description='营业部名称')
    trade_date: datetime.date | None = Field(default=datetime.date.today(), description='上榜日', index=True)
    buy_stock_count: int | None = Field(default=None, description='买入个股数')
    sell_stock_count: int | None = Field(default=None, description='卖出个股数')

    buy_amount_total: float | None = Field(default=None, description='买入总金额')
    sell_amount_total: float | None = Field(default=None, description='卖出总金额')
    net_amount_total: float | None = Field(default=None, description='总买卖净额')
    buy_stocks: str | None = Field(max_length=400, description='买入股票')

    created_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='创建时间', index=True)
    updated_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='更新时间', index=True)


class StockLhbHyyybEm(StockLhbHyyybEmBase, table=True):
    """stock_lhb_hyyyb_em表"""
    __tablename__ = "stock_lhb_hyyyb_em"
    id: int | None = Field(default=None, primary_key=True, description='id')


class StockLhbHyyybEmCreate(StockLhbHyyybEmBase):
    pass


class StockLhbHyyybEmPublic(StockLhbHyyybEmBase):
    id: int


class StockLhbHyyybEmAllPublic(SQLModel):
    data: list[StockLhbHyyybEmPublic]
    count: int
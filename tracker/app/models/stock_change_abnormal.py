# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_change_abnormal
   Description : 盘口异动
   Author :       EveryFine
   Date：          2024/7/16
-------------------------------------------------
   Change Activity:
                   2024/7/16:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

import datetime

from sqlmodel import SQLModel, Field


class StockChangeAbnormalBase(SQLModel):
    symbol: str = Field(max_length=20, description='股票代码', index=True)
    date: datetime.date | None = Field(default=datetime.date.today(), description='日期', index=True)
    event_time: datetime.time | None = Field(default=None, description='事件发生时间', index=True)
    name: str | None = Field(max_length=40, description='股票名称')
    event: str | None = Field(max_length=40, description='事件')
    attach_info: str | None = Field(max_length=40, description='事件')
    created_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='创建时间', index=True)
    updated_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='更新时间', index=True)


class StockChangeAbnormal(StockChangeAbnormalBase, table=True):
    """stock_change_abnormal表"""
    __tablename__ = "stock_change_abnormal"
    id: int | None = Field(default=None, primary_key=True, description='id')


class StockChangeAbnormalCreate(StockChangeAbnormalBase):
    pass


class StockChangeAbnormalPublic(StockChangeAbnormalBase):
    id: int


class StockChangeAbnormalAllPublic(SQLModel):
    data: list[StockChangeAbnormalPublic]
    count: int

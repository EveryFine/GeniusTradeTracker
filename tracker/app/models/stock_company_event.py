# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_company_event
   Description : 公司动态
   Author :       EveryFine
   Date：          2024/7/21
-------------------------------------------------
   Change Activity:
                   2024/7/21:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

import datetime

from sqlmodel import SQLModel, Field


class StockCompanyEventBase(SQLModel):
    symbol: str = Field(max_length=20, description='股票代码', index=True)
    event_date: datetime.date | None = Field(default=datetime.date.today(), description='事件日期', index=True)
    date_index: int | None = Field(default=None, description='当天序号')
    name: str | None = Field(max_length=20, description='股票名称')
    event_type: str | None = Field(max_length=20, description='事件类型')
    event: str | None = Field(max_length=5000, description='具体事项')
    created_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='创建时间', index=True)
    updated_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='更新时间', index=True)


class StockCompanyEvent(StockCompanyEventBase, table=True):
    """stock_company_event表"""
    __tablename__ = "stock_company_event"
    id: int | None = Field(default=None, primary_key=True, description='id')


class StockCompanyEventCreate(StockCompanyEventBase):
    pass


class StockCompanyEventPublic(StockCompanyEventBase):
    id: int


class StockCompanyEventsPublic(SQLModel):
    data: list[StockCompanyEventPublic]
    count: int

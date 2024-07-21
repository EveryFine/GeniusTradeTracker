# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_news
   Description :  个股新闻
   Author :       EveryFine
   Date：          2024/7/15
-------------------------------------------------
   Change Activity:
                   2024/7/15:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

import datetime

from sqlmodel import SQLModel, Field


class StockNewsBase(SQLModel):
    symbol: str = Field(max_length=20, description='股票代码', index=True)
    pub_time: datetime.datetime | None = Field(default=datetime.datetime.now(), description='发布时间', index=True)
    title: str | None = Field(max_length=200, description='新闻标题')
    content: str | None = Field(max_length=1000, description='新闻内容')
    source: str | None = Field(max_length=50, description='文章来源')
    link: str | None = Field(max_length=500, description='新闻链接')
    created_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='创建时间', index=True)
    updated_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='更新时间', index=True)


class StockNews(StockNewsBase, table=True):
    """stock_news表"""
    __tablename__ = "stock_news"
    id: int | None = Field(default=None, primary_key=True, description='id')


class StockNewsCreate(StockNewsBase):
    pass


class StockNewsPublic(StockNewsBase):
    id: int


class StockNewsAllPublic(SQLModel):
    data: list[StockNewsPublic]
    count: int

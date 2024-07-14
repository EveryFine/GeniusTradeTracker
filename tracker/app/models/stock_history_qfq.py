# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_history_qfq
   Description : 股票历史行情，前复权
   Author :       EveryFine
   Date：          2024/7/14
-------------------------------------------------
   Change Activity:
                   2024/7/14:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

from sqlmodel import Field, SQLModel

from app.models.stock_history import StockHistoryBase


class StockHistoryQfqBase(StockHistoryBase):
    pass


class StockHistoryQfq(StockHistoryQfqBase, table=True):
    """stock_history_qfq表"""
    __tablename__ = "stock_history_qfq"
    id: int | None = Field(default=None, primary_key=True, description='id')


class StockHistoryQfqCreate(StockHistoryQfqBase):
    pass


class StockHistoryQfqPublic(StockHistoryQfqBase):
    id: int


class StockHistoriesQfqPublic(SQLModel):
    data: list[StockHistoryQfqPublic]
    count: int

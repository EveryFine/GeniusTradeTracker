# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_history_hfq
   Description :   股票历史行情，后复权
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


class StockHistoryHfqBase(StockHistoryBase):
    pass


class StockHistoryHfq(StockHistoryHfqBase, table=True):
    """stock_history_qfq表"""
    __tablename__ = "stock_history_hfq"
    id: int | None = Field(default=None, primary_key=True, description='id')


class StockHistoryHfqCreate(StockHistoryHfqBase):
    pass


class StockHistoryHfqPublic(StockHistoryHfqBase):
    id: int


class StockHistoriesHfqPublic(SQLModel):
    data: list[StockHistoryHfqPublic]
    count: int

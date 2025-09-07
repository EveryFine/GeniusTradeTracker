# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_zh_a_spot_em
   Description :
   Author :       EveryFine
   Date：          2025/9/7
-------------------------------------------------
   Change Activity:
                   2025/9/7:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

from sqlmodel import Field, SQLModel

from app.models.stock_zh_a_spot_em_realtime import StockZhASpotEmRealtimeBase


class StockZhASpotEm(StockZhASpotEmRealtimeBase, table=True):
    """stock_zh_a_spot_em表"""
    __tablename__ = "stock_zh_a_spot_em"
    id: int | None = Field(default=None, primary_key=True, description='id')


class StockZhASpotEmCreate(StockZhASpotEmRealtimeBase):
    pass


class StockZhASpotEmPublic(StockZhASpotEmRealtimeBase):
    id: int


class StockZhASpotEmAllPublic(SQLModel):
    data: list[StockZhASpotEmPublic]
    count: int
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_board_industry_em_realtime
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

from app.models.stock_board_industry_em import StockBoardIndustryEmBase


class StockBoardIndustryEmRealtime(StockBoardIndustryEmBase, table=True):
    """stock_board_industry_em_realtime表"""
    __tablename__ = "stock_board_industry_em_realtime"
    id: int | None = Field(default=None, primary_key=True, description='id')


class StockBoardIndustryEmRealtimeCreate(StockBoardIndustryEmBase):
    pass


class StockBoardIndustryEmRealtimePublic(StockBoardIndustryEmBase):
    id: int


class StockBoardIndustryEmAllPublic(SQLModel):
    data: list[StockBoardIndustryEmRealtimePublic]
    count: int
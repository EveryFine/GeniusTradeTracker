# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_board_concept_em_realtime
   Description :  方财富网-行情中心-沪深京板块-概念板块-实时
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

from app.models.stock_board_concept_em import StockBoardConceptEmBase


class StockBoardConceptEmRealtime(StockBoardConceptEmBase, table=True):
    """stock_board_concept_em_realtime表"""
    __tablename__ = "stock_board_concept_em_realtime"
    id: int | None = Field(default=None, primary_key=True, description='id')


class StockBoardConceptEmRealtimeCreate(StockBoardConceptEmBase):
    pass


class StockBoardConceptEmRealtimePublic(StockBoardConceptEmBase):
    id: int


class StockBoardConceptEmAllPublic(SQLModel):
    data: list[StockBoardConceptEmRealtimePublic]
    count: int
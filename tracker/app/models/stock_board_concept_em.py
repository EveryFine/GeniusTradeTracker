# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_board_concept_em
   Description : 东方财富-概念板块
                 接口: stock_board_concept_name_em
                 目标地址: https://quote.eastmoney.com/center/boardlist.html#concept_board
                 描述: 东方财富网-行情中心-沪深京板块-概念板块
   Author :       EveryFine
   Date：          2025/9/7
-------------------------------------------------
   Change Activity:
                   2025/9/7:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

import datetime

from sqlmodel import SQLModel, Field


class StockBoardConceptEmBase(SQLModel):
    trade_date: datetime.date | None = Field(default=datetime.date.today(), description='日期', index=True)
    collect_time: datetime.datetime | None = Field(default_factory=lambda: datetime.datetime.now(),
                                                   description='采集时间', index=True)
    rank: int | None = Field(default=None, description='排名')
    name: str | None = Field(max_length=40, description='板块名称')
    symbol: str | None = Field(max_length=40, description='板块代码')
    latest_price: float | None = Field(default=None, description='最新价')
    change_amount: float | None = Field(default=None, description='涨跌额')
    change_rate: float | None = Field(default=None, description='涨跌幅')
    market_value: float | None = Field(default=None, description='总市值')
    turnover_rate: float | None = Field(default=None, description='换手率')

    sz_count: int | None = Field(default=None, description='上涨家数')
    xd_count: int | None = Field(default=None, description='下跌家数')
    lz_symbol: str | None = Field(max_length=40, description='领涨股票')
    lz_symbol_change_rate: float | None = Field(default=None, description='领涨股票-涨跌幅')

    created_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='创建时间', index=True)
    updated_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='更新时间', index=True)


class StockBoardConceptEm(StockBoardConceptEmBase, table=True):
    """stock_board_concept_em表"""
    __tablename__ = "stock_board_concept_em"
    id: int | None = Field(default=None, primary_key=True, description='id')


class StockBoardConceptEmCreate(StockBoardConceptEmBase):
    pass


class StockBoardConceptEmPublic(StockBoardConceptEmBase):
    id: int


class StockBoardConceptEmAllPublic(SQLModel):
    data: list[StockBoardConceptEmPublic]
    count: int

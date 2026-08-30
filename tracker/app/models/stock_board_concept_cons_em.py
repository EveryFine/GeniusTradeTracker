# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_board_concept_cons_em
   Description :   东方财富-概念-成份股
                接口: stock_board_concept_cons_em
                目标地址: http://quote.eastmoney.com/center/boardlist.html#boards-BK06551
                描述: 东方财富-沪深板块-概念板块-板块成份

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


class StockBoardConceptConsEmBase(SQLModel):
    trade_date: datetime.date | None = Field(default=datetime.date.today(), description='日期', index=True)
    collect_time: datetime.datetime | None = Field(default_factory=lambda: datetime.datetime.now(),
                                                   description='采集时间', index=True)
    board_name: str | None = Field(max_length=40, description='概念名称')
    board_symbol: str | None = Field(max_length=40, description='概念代码')
    stock_name: str | None = Field(max_length=40, description='成分股名称')
    stock_symbol: str | None = Field(max_length=40, description='成分股代码')

    stock_index: str | None = Field(max_length=40, description='序号')

    latest_price: float | None = Field(default=None, description='最新价')
    change_rate: float | None = Field(default=None, description='涨跌幅')
    change_amount: float | None = Field(default=None, description='涨跌额')

    volume: int | None = Field(default=None, description='成交量')
    turnover: float | None = Field(default=None, description='成交额')
    range: float | None = Field(default=None, description='振幅')
    high: float | None = Field(default=None, description='最高')
    low: float | None = Field(default=None, description='最低')
    open: float | None = Field(default=None, description='今开')
    pre_close: float | None = Field(default=None, description='昨收')
    turnover_rate: float | None = Field(default=None, description='换手率')
    forward_pe_ratio: float | None = Field(default=None, description='市盈率-动态')
    pb_mrq: float | None = Field(default=None, description='市净率')

    created_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='创建时间', index=True)
    updated_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='更新时间', index=True)


class StockBoardConceptConsEm(StockBoardConceptConsEmBase, table=True):
    """stock_board_concept_cons_em表"""
    __tablename__ = "stock_board_concept_cons_em"
    id: int | None = Field(default=None, primary_key=True, description='id')


class StockBoardConceptConsEmCreate(StockBoardConceptConsEmBase):
    pass


class StockBoardConceptConsEmPublic(StockBoardConceptConsEmBase):
    id: int


class StockBoardConceptConsEmAllPublic(SQLModel):
    data: list[StockBoardConceptConsEmPublic]
    count: int
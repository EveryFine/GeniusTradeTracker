# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_fund_concept_detail_rank
   Description :  资金流--概念--详细--排行
   Author :       EveryFine
   Date：          2024/7/28
-------------------------------------------------
   Change Activity:
                   2024/7/28:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

import datetime

from sqlmodel import SQLModel, Field


class StockFundConceptDetailRankBase(SQLModel):
    trade_date: datetime.date | None = Field(default=datetime.date.today(), description='日期', index=True)
    range_type: str = Field(max_length=20, description='排行类型: 5日，10日', index=True)
    name: str | None = Field(max_length=40, description='名称')
    change_rate: float | None = Field(default=None, description='涨跌幅')

    main_in_rank: float | None = Field(default=None, description='主力净流入排名')
    main_in_net: float | None = Field(default=None, description='主力净流入-净额')
    main_in_per: float | None = Field(default=None, description='主力净流入-净占比')
    main_in_most_stock: str | None = Field(max_length=40, description='主力净流入最大股')

    huge_in_net: float | None = Field(default=None, description='超大单净流入-净额')
    huge_in_per: float | None = Field(default=None, description='超大单净流入-净占比')

    big_in_net: float | None = Field(default=None, description='大单净流入-净额')
    big_in_per: float | None = Field(default=None, description='大单净流入-净占比')

    middle_in_net: float | None = Field(default=None, description='中单净流入-净额')
    middle_in_per: float | None = Field(default=None, description='中单净流入-净占比')

    small_in_net: float | None = Field(default=None, description='小单净流入-净额')
    small_in_per: float | None = Field(default=None, description='小单净流入-净占比')

    created_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='创建时间', index=True)
    updated_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='更新时间', index=True)


class StockFundConceptDetailRank(StockFundConceptDetailRankBase, table=True):
    """stock_fund_concept_detail_rank表"""
    __tablename__ = "stock_fund_concept_detail_rank"
    id: int | None = Field(default=None, primary_key=True, description='id')


class StockFundConceptDetailRankCreate(StockFundConceptDetailRankBase):
    pass


class StockFundConceptDetailRankPublic(StockFundConceptDetailRankBase):
    id: int


class StockFundConceptDetailRankAllPublic(SQLModel):
    data: list[StockFundConceptDetailRankPublic]
    count: int

# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_fund_industry_rank
   Description :  资金流 -- 行业 -- 排行
   Author :       EveryFine
   Date：          2024/7/27
-------------------------------------------------
   Change Activity:
                   2024/7/27:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

import datetime

from sqlmodel import SQLModel, Field


class StockFundIndustryRankBase(SQLModel):
    trade_date: datetime.date | None = Field(default=datetime.date.today(), description='日期', index=True)
    range_type: str = Field(max_length=20, description='排行类型：3日，5日，10日，20日', index=True)
    name: str | None = Field(max_length=40, description='概念名称')
    firm_number: int | None = Field(default=None, description='公司家数')
    index: float | None = Field(default=None, description='概念指数')
    change_rate: float | None = Field(default=None, description='阶段涨跌幅')
    change_rate_rank: float | None = Field(default=None, description='阶段涨跌幅排名')
    fund_in: float | None = Field(default=None, description='流入资金')
    fund_out: float | None = Field(default=None, description='流出资金')
    net_amount: float | None = Field(default=None, description='净额')
    created_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='创建时间', index=True)
    updated_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='更新时间', index=True)


class StockFundIndustryRank(StockFundIndustryRankBase, table=True):
    """stock_fund_industry_rank表"""
    __tablename__ = "stock_fund_industry_rank"
    id: int | None = Field(default=None, primary_key=True, description='id')


class StockFundIndustryRankCreate(StockFundIndustryRankBase):
    pass


class StockFundIndustryRankPublic(StockFundIndustryRankBase):
    id: int


class StockFundIndustryRankAllPublic(SQLModel):
    data: list[StockFundIndustryRankPublic]
    count: int
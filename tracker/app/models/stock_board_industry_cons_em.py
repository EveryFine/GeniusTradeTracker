# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_board_industry_cons_em
   Description :  东方财富-行业板块-成份股
                接口: stock_board_industry_cons_em
                目标地址: https://data.eastmoney.com/bkzj/BK1027.html
                描述: 东方财富-沪深板块-行业板块-板块成份
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


class StockBoardIndustryConsEmBase(SQLModel):
    board_name: str | None = Field(max_length=40, description='板块名称')
    board_symbol: str | None = Field(max_length=40, description='板块代码')
    stock_name: str | None = Field(max_length=40, description='成分股名称')
    stock_symbol: str | None = Field(max_length=40, description='成分股代码')

    created_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='创建时间', index=True)
    updated_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='更新时间', index=True)


class StockBoardIndustryConsEm(StockBoardIndustryConsEmBase, table=True):
    """stock_board_industry_cons_em表"""
    __tablename__ = "stock_board_industry_cons_em"
    id: int | None = Field(default=None, primary_key=True, description='id')


class StockBoardIndustryConsEmCreate(StockBoardIndustryConsEmBase):
    pass


class StockBoardIndustryConsEmPublic(StockBoardIndustryConsEmBase):
    id: int


class StockBoardIndustryConsEmAllPublic(SQLModel):
    data: list[StockBoardIndustryConsEmPublic]
    count: int
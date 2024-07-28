# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_fund_market_detail
   Description :  资金流--大盘
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


class StockFundMarketDetailBase(SQLModel):
    trade_date: datetime.date | None = Field(default=datetime.date.today(), description='日期', index=True)

    sh_close: float | None = Field(default=None, description='上证-收盘价')
    sh_change_rate: float | None = Field(default=None, description='上证-涨跌幅')

    sz_close: float | None = Field(default=None, description='深证-收盘价')
    sz_change_rate: float | None = Field(default=None, description='深证-涨跌幅')

    main_in_net: float | None = Field(default=None, description='主力净流入-净额')
    main_in_per: float | None = Field(default=None, description='主力净流入-净占比')

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


class StockFundMarketDetail(StockFundMarketDetailBase, table=True):
    """stock_fund_market_detail表"""
    __tablename__ = "stock_fund_market_detail"
    id: int | None = Field(default=None, primary_key=True, description='id')


class StockFundMarketDetailCreate(StockFundMarketDetailBase):
    pass


class StockFundMarketDetailPublic(StockFundMarketDetailBase):
    id: int


class StockFundMarketDetailAllPublic(SQLModel):
    data: list[StockFundMarketDetailPublic]
    count: int

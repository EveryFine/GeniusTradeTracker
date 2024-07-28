# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_fund_single_detail_intraday
   Description :   资金流 -- 个股 -- 详细 -- 即时
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
class StockFundSingleDetailIntradayBase(SQLModel):
    trade_date: datetime.date | None = Field(default=datetime.date.today(), description='日期', index=True)
    symbol: str = Field(max_length=20, description='股票代码', index=True)
    name: str | None = Field(max_length=40, description='股票名称')
    latest_price: float | None = Field(default=None, description='最新价')
    change_rate: float | None = Field(default=None, description='涨跌幅')
    
    main_in_rank: float | None = Field(default=None, description='当天主力净流入排名')
    main_in_net: float | None = Field(default=None, description='今日主力净流入-净额')
    main_in_per: float | None = Field(default=None, description='今日主力净流入-净占比')
    
    huge_in_net: float | None = Field(default=None, description='今日超大单净流入-净额')
    huge_in_per: float | None = Field(default=None, description='今日超大单净流入-净占比')

    big_in_net: float | None = Field(default=None, description='今日大单净流入-净额')
    big_in_per: float | None = Field(default=None, description='今日大单净流入-净占比')

    middle_in_net: float | None = Field(default=None, description='今日中单净流入-净额')
    middle_in_per: float | None = Field(default=None, description='今日中单净流入-净占比')

    small_in_net: float | None = Field(default=None, description='今日小单净流入-净额')
    small_in_per: float | None = Field(default=None, description='今日小单净流入-净占比')
    
    created_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='创建时间', index=True)
    updated_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='更新时间', index=True)

class StockFundSingleDetailIntraday(StockFundSingleDetailIntradayBase, table=True):
    """stock_fund_single_detail_intraday表"""
    __tablename__ = "stock_fund_single_detail_intraday"
    id: int | None = Field(default=None, primary_key=True, description='id')


class StockFundSingleDetailIntradayCreate(StockFundSingleDetailIntradayBase):
    pass


class StockFundSingleDetailIntradayPublic(StockFundSingleDetailIntradayBase):
    id: int


class StockFundSingleDetailIntradayAllPublic(SQLModel):
    data: list[StockFundSingleDetailIntradayPublic]
    count: int
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_history_bao_k
   Description :
   Author :       EveryFine
   Date：          2025/5/2
-------------------------------------------------
   Change Activity:
                   2025/5/2:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

import datetime

from sqlmodel import SQLModel, Field
from sqlalchemy import Column, BigInteger


class StockHistoryBaoKBase(SQLModel):
    code: str = Field(max_length=20, description='股票代码，待市场标识', index=True)
    symbol: str = Field(max_length=20, description='股票代码，不带市场标识')
    name: str | None = Field(max_length=40, description='股票名称')
    date: datetime.date | None = Field(default=datetime.date.today(), description='日期', index=True)
    open: float | None = Field(default=None, description='开盘价')
    close: float | None = Field(default=None, description='收盘价')
    high: float | None = Field(default=None, description='最高价')
    low: float | None = Field(default=None, description='最低价')
    volume: int | None = Field(default=None, description='成交量', sa_column=Column(BigInteger))
    pre_close: float | None = Field(default=None, description='前收盘价')
    amount: float | None = Field(default=None, description='成交额（单位：人民币元）')
    adjust_flag: int | None = Field(default=None, description='复权状态(1：后复权， 2：前复权，3：不复权）此表全为3')
    turn: float | None = Field(default=None, description='换手率')
    trade_status: int | None = Field(default=None, description='交易状态(1：正常交易 0：停牌）')
    change_rate: float | None = Field(default=None, description='涨跌幅（百分比）')
    pe_ttm: float | None = Field(default=None, description='滚动市盈率')
    pb_mrq: float | None = Field(default=None, description='市净率')
    ps_ttm: float | None = Field(default=None, description='滚动市销率')
    pcf_ncf_ttm: float | None = Field(default=None, description='滚动市现率')
    is_st: int | None = Field(default=None, description='是否ST股，1是，0否')

    created_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='创建时间', index=True)
    updated_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='更新时间', index=True)


class StockHistoryBaoK(StockHistoryBaoKBase, table=True):
    """stock_history_bao_k表"""
    __tablename__ = "stock_history_bao_k"
    id: int | None = Field(default=None, primary_key=True, description='id')


class StockHistoryBaoKCreate(StockHistoryBaoKBase):
    pass


class StockHistoryBaoKPublic(StockHistoryBaoKBase):
    id: int


class StockHistoryBaoKsPublic(SQLModel):
    data: list[StockHistoryBaoKPublic]
    count: int

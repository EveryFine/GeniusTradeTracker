# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     crud_stock_exchange
   Description :
   Author :       EveryFine
   Date：          2024/6/30
-------------------------------------------------
   Change Activity:
                   2024/6/30:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

from typing import List

from fastapi import Query
from sqlmodel import Session, select, func

from app.models.stock_exchange import StockExchange, StockExchangesPublic, StockExchangeCreate

import pandas as pd
import akshare as ak


def get_stock_exchanges(*, session: Session,  offset: int = 0,limit: int = Query(default=100, le=100)) -> StockExchangesPublic:
    count_statement = select(func.count()).select_from(StockExchange)
    count = session.exec(count_statement).one()

    statement = select(StockExchange).offset(offset).limit(limit)
    stock_exchanges = session.exec(statement).all()

    return StockExchangesPublic(data=stock_exchanges, count=count)


def create_stock_exchanges(*, session: Session) -> List[StockExchange]:
    df = pd.read_csv('stock_exchange_list.csv')
    res=[]
    for row in df.rows:
        db_stock_exchange = create_stock_exchange(row, session)
        res.append(db_stock_exchange)
    return res


def create_stock_exchange(row, session):
    stock_exchange_create = StockExchangeCreate()
    stock_exchange_create.name = row['name']
    stock_exchange_create.city = row['city']
    stock_exchange_create.akshare_abb = row['akshare']
    stock_exchange_create.yfinance_abb = row['yfinance']
    # 获取股票数量信息
    if row['name'] == '上交所':
        stock_sse_summary_df = ak.stock_sse_summary()
        stock_count_sse = stock_sse_summary_df['项目' == '上市股票']['股票']
        stock_exchange_create.stock_count = stock_count_sse
    if row['name'] == '深交所':
        # todo: 待交易日接口完成后，此处date参数采用该接口获取最后一个交易日
        stock_szse_summary_df = ak.stock_szse_summary(date="20240628")
        stock_count_szse = stock_szse_summary_df['证券类别' == '股票']['数量']
        stock_exchange_create.stock_count = stock_count_szse
    db_stock_exchange = StockExchange.model_validate(stock_exchange_create)
    session.add(db_stock_exchange)
    session.commit()
    session.refresh(db_stock_exchange)
    return db_stock_exchange
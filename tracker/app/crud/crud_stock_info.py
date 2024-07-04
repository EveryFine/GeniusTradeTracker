# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     crud_stock_info
   Description :
   Author :       EveryFine
   Date：          2024/7/3
-------------------------------------------------
   Change Activity:
                   2024/7/3:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

from datetime import datetime
from typing import List

from fastapi import Query
from sqlmodel import Session, select, func

from app.models.stock_info import StockInfo, StockInfoCreate, StockInfosPublic
import akshare as ak


def get_stock_infos(*, session: Session, offset: int = 0,
                    limit: int = Query(default=100, le=100)) -> StockInfosPublic:
    count_statement = select(func.count()).select_from(StockInfo)
    count = session.exec(count_statement).one()

    statement = select(StockInfo).offset(offset).limit(limit)
    stock_exchanges = session.exec(statement).all()

    return StockInfosPublic(data=stock_exchanges, count=count)


def create_stock_infos(*, session: Session) -> List[StockInfo]:
    res = []
    res_sh = create_sh_stocks(session)
    res.append(res_sh)
    res_sz = create_sz_stocks(session)
    res.append(res_sz)
    return res


def create_sh_stocks(session):
    stock_info_sh_name_code_df = ak.stock_info_sh_name_code(symbol="主板A股")
    res = []
    for index, row in stock_info_sh_name_code_df.iterrows():
        db_stock_info = create_sh_stock_info(session, row)
        res.append(db_stock_info)
    return res


def create_sz_stocks(session):
    stock_info_sz_name_code_df = ak.stock_info_sz_name_code(symbol="A股列表")
    res = []
    for index, row in stock_info_sz_name_code_df.iterrows():
        db_stock_info_sz = create_sz_stock_info(session, row)
        res.append(db_stock_info_sz)

    return res


def create_sh_stock_info(session, row) -> StockInfo:
    symbol = row['证券代码']
    res = create_stock_info_by_symbol(session, symbol, exchange='sh')
    return res


def create_sz_stock_info(session, row):
    symbol = row['A股代码']
    res = create_stock_info_by_symbol(session, symbol, exchange='sz')
    return res


def create_stock_info_by_symbol(session, symbol, exchange):
    df = ak.stock_individual_info_em(symbol=symbol)
    short_name = df.loc[df['item'] == '股票简称', 'value'].values[0]
    market_value = df.loc[df['item'] == '总市值', 'value'].values[0]
    traded_market_value = df.loc[df['item'] == '流通市值', 'value'].values[0]
    industry = df.loc[df['item'] == '行业', 'value'].values[0]
    date_str = df.loc[df['item'] == '上市时间', 'value'].values[0]
    offering_date = datetime.strptime(str(date_str), "%Y%m%d").date()
    total_share_capital = df.loc[df['item'] == '总股本', 'value'].values[0]
    outstanding_shares = df.loc[df['item'] == '流通股', 'value'].values[0]
    stock_info_create = StockInfoCreate(symbol=symbol, market_value=market_value,
                                        traded_market_value=traded_market_value, industry=industry,
                                        offering_date=offering_date, short_name=short_name,
                                        total_share_capital=total_share_capital, outstanding_shares=outstanding_shares,
                                        exchange=exchange)
    db_stock_info = StockInfo.model_validate(stock_info_create)
    session.add(db_stock_info)
    session.commit()
    session.refresh(db_stock_info)
    res = StockInfo.model_validate(db_stock_info)
    return res

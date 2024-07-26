# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     crud_stock_rank_xstp
   Description :    技术指标 -- 向上突破
   Author :       EveryFine
   Date：          2024/7/21
-------------------------------------------------
   Change Activity:
                   2024/7/21:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

import datetime

import akshare as ak
from sqlmodel import Session, select

from app.common.log import log
from app.crud.crud_stock_trade_date import get_last_trade_date

from app.models.stock_rank_xstp import StockRankXstp


def create_stock_rank_xstp(*, session: Session) -> int:
    range_types = (
        "5日均线", "10日均线", "20日均线", "30日均线", "60日均线", "90日均线", "250日均线", "500日均线")
    xstp_count = create_rank_xstp_by_types(session, range_types)
    return xstp_count


def create_rank_xstp_by_types(session, range_types):
    created_count = 0
    for range_type in range_types:
        res = create_stock_rank_xstp_type(session, range_type)
        created_count += res
        session.commit()
        log.info(f'creat stock rank xstp by range type finish, type:{range_type}, created count: {res}')
    session.commit()
    log.info(f'creat stock rank xstp finish, created count: {created_count}')
    return created_count


def create_stock_rank_xstp_type(session, range_type):
    xstp_type_count = 0
    trade_date = get_last_trade_date(session=session, final_datetime=datetime.datetime.now())
    stock_rank_xstp_ths_df = ak.stock_rank_xstp_ths(symbol=range_type)
    for index, row in stock_rank_xstp_ths_df.iterrows():
        res = create_stock_rank_xstp_item(session, trade_date, range_type, row)
        xstp_type_count += res
    return xstp_type_count


def create_stock_rank_xstp_item(session, trade_date, range_type, row):
    symbol = row['股票代码']
    name = row['股票简称']
    latest_price = row['最新价']

    change_rate = row['涨跌幅']
    turnover_rate = row['换手率']

    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()

    items_saved = get_stock_rank_xstp_items(session, symbol, range_type, trade_date)
    if items_saved is None or len(items_saved) == 0:
        stock_rank_xstp_create = StockRankXstp(trade_date=trade_date, range_type=range_type, symbol=symbol, name=name, latest_price=latest_price, change_rate=change_rate, turnover_rate=turnover_rate, created_at=created_at, updated_at=updated_at)
        db_stock_rank_xstp = StockRankXstp.model_validate(stock_rank_xstp_create)
        session.add(db_stock_rank_xstp)
        return 1
    else:
        return 0


def get_stock_rank_xstp_items(session, symbol, range_type, trade_date):
    statement = (select(StockRankXstp).where(StockRankXstp.symbol == symbol).
                 where(StockRankXstp.trade_date == trade_date).
                 where(StockRankXstp.range_type == range_type))
    items = session.execute(statement).all()
    return items
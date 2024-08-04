# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     crud_stock_rank_xxtp
   Description :
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
from app.crud.crud_stock_trade_date import get_last_trade_date, get_last_trade_date_by_date

from app.models.stock_rank_xxtp import StockRankXxtp


def create_stock_rank_xxtp(*, session: Session) -> int:
    range_types = (
        "5日均线", "10日均线", "20日均线", "30日均线", "60日均线", "90日均线", "250日均线", "500日均线")
    xxtp_count = create_rank_xxtp_by_types(session, range_types)
    return xxtp_count


def create_rank_xxtp_by_types(session, range_types):
    created_count = 0
    for range_type in range_types:
        res = create_stock_rank_xxtp_type(session, range_type)
        created_count += res
        session.commit()
        log.info(f'creat stock rank xxtp by range type finish, type:{range_type}, created count: {res}')
    session.commit()
    log.info(f'creat stock rank xxtp finish, created count: {created_count}')
    return created_count


def create_stock_rank_xxtp_type(session, range_type):
    xxtp_type_count = 0
    trade_date = get_last_trade_date(session=session, final_datetime=datetime.datetime.now())
    stock_rank_xxtp_ths_df = ak.stock_rank_xxtp_ths(symbol=range_type)
    for index, row in stock_rank_xxtp_ths_df.iterrows():
        res = create_stock_rank_xxtp_item(session, trade_date, range_type, row)
        xxtp_type_count += res
    return xxtp_type_count


def create_stock_rank_xxtp_item(session, trade_date, range_type, row):
    symbol = row['股票代码']
    name = row['股票简称']
    latest_price = row['最新价']

    change_rate = row['涨跌幅']
    turnover_rate = row['换手率']

    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()

    items_saved = get_stock_rank_xxtp_items(session, symbol, range_type, trade_date)
    if items_saved is None or len(items_saved) == 0:
        stock_rank_xxtp_create = StockRankXxtp(trade_date=trade_date, range_type=range_type, symbol=symbol, name=name,
                                               latest_price=latest_price, change_rate=change_rate,
                                               turnover_rate=turnover_rate, created_at=created_at,
                                               updated_at=updated_at)
        db_stock_rank_xxtp = StockRankXxtp.model_validate(stock_rank_xxtp_create)
        session.add(db_stock_rank_xxtp)
        return 1
    else:
        return 0


def get_stock_rank_xxtp_items(session, symbol, range_type, trade_date):
    statement = (select(StockRankXxtp).where(StockRankXxtp.symbol == symbol).
                 where(StockRankXxtp.trade_date == trade_date).
                 where(StockRankXxtp.range_type == range_type))
    items = session.execute(statement).all()
    return items


def check_stock_rank_xxtp_date(session, check_date):
    last_trade_date = get_last_trade_date_by_date(session=session, final_date=check_date)
    statement = select(StockRankXxtp).where(
        StockRankXxtp.trade_date == last_trade_date)
    items = session.execute(statement).all()
    if items is None or len(items) == 0:
        return False
    else:
        return True

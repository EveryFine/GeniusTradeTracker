# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     crud_stock_rank_cxd
   Description :   技术指标 -- 创新低
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

from app.models.stock_rank_cxd import StockRankCxd


def create_stock_rank_cxd(*, session: Session) -> int:
    range_types = (
        "创月新低", "半年新低", "一年新低", "历史新低")
    cxd_count = create_rank_cxd_by_types(session, range_types)
    return cxd_count


def create_rank_cxd_by_types(session, range_types):
    created_count = 0
    for range_type in range_types:
        res = create_stock_rank_cxd_type(session, range_type)
        created_count += res
        session.commit()
        log.info(f'creat stock rank cxd by range type finish, type:{range_type}, created count: {res}')
    session.commit()
    log.info(f'creat stock rank cxd finish, created count: {created_count}')
    return created_count


def create_stock_rank_cxd_type(session, range_type):
    cxd_type_count = 0
    trade_date = get_last_trade_date(session=session, date=datetime.date.today())
    stock_rank_cxd_ths_df = ak.stock_rank_cxd_ths(symbol=range_type)
    for index, row in stock_rank_cxd_ths_df.iterrows():
        res = create_stock_rank_cxd_item(session, trade_date, range_type, row)
        cxd_type_count += res
    return cxd_type_count


def create_stock_rank_cxd_item(session, trade_date, range_type, row):
    symbol = row['股票代码']
    name = row['股票简称']
    change_rate = row['涨跌幅']
    turnover_rate = row['换手率']
    latest_price = row['最新价']
    pre_low = row['前期低点']
    pre_low_date = row['前期低点日期']
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()

    items_saved = get_stock_rank_cxd_items(session, symbol, range_type, trade_date)
    if items_saved is None or len(items_saved) == 0:
        stock_rank_cxd_create = StockRankCxd(trade_date=trade_date, range_type=range_type, symbol=symbol, name=name,
                                             change_rate=change_rate, turnover_rate=turnover_rate,
                                             latest_price=latest_price, pre_low=pre_low, pre_low_date=pre_low_date,
                                             created_at=created_at, updated_at=updated_at)
        db_stock_rank_cxd = StockRankCxd.model_validate(stock_rank_cxd_create)
        session.add(db_stock_rank_cxd)
        return 1
    else:
        return 0


def get_stock_rank_cxd_items(session, symbol, range_type, trade_date):
    statement = (select(StockRankCxd).where(StockRankCxd.symbol == symbol).
                 where(StockRankCxd.trade_date == trade_date).
                 where(StockRankCxd.range_type == range_type))
    items = session.execute(statement).all()
    return items

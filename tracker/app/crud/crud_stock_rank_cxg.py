# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     crud_stock_rank_cxg
   Description :   技术指标 -- 创新高
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
from app.models.stock_rank_cxg import StockRankCxg


def create_stock_rank_cxg(*, session: Session) -> int:
    range_types = (
        "创月新高", "半年新高", "一年新高", "历史新高")
    cxg_count = create_rank_cxg_by_types(session, range_types)
    return cxg_count


def create_rank_cxg_by_types(session, range_types):
    created_count = 0
    for range_type in range_types:
        res = create_stock_rank_cxg_type(session, range_type)
        created_count += res
        session.commit()
        log.info(f'creat stock rank cxg by range type finish, type:{range_type}, created count: {res}')
    session.commit()
    log.info(f'creat stock rank cxg finish, created count: {created_count}')
    return created_count


def create_stock_rank_cxg_type(session, range_type):
    cxg_type_count = 0
    trade_date = get_last_trade_date(session=session, date=datetime.date.today())
    stock_rank_cxg_ths_df = ak.stock_rank_cxg_ths(symbol=range_type)
    for index, row in stock_rank_cxg_ths_df.iterrows():
        res = create_stock_rank_cxg_item(session, trade_date, range_type, row)
        cxg_type_count += res
    return cxg_type_count


def create_stock_rank_cxg_item(session, trade_date, range_type, row):
    symbol = row['股票代码']
    name = row['股票简称']
    change_rate = row['涨跌幅']
    turnover_rate = row['换手率']
    latest_price = row['最新价']
    pre_high = row['前期高点']
    pre_high_date = row['前期高点日期']
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()

    items_saved = get_stock_rank_cxg_items(session, symbol, range_type, trade_date)
    if items_saved is None or len(items_saved) == 0:
        stock_rank_cxg_create = StockRankCxg(trade_date=trade_date, range_type=range_type, symbol=symbol, name=name,
                                             change_rate=change_rate, turnover_rate=turnover_rate,
                                             latest_price=latest_price, pre_high=pre_high, pre_high_date=pre_high_date,
                                             created_at=created_at, updated_at=updated_at)
        db_stock_rank_cxg = StockRankCxg.model_validate(stock_rank_cxg_create)
        session.add(db_stock_rank_cxg)
        return 1
    else:
        return 0


def get_stock_rank_cxg_items(session, symbol, range_type, trade_date):
    statement = (select(StockRankCxg).where(StockRankCxg.symbol == symbol).
                 where(StockRankCxg.trade_date == trade_date).
                 where(StockRankCxg.range_type == range_type))
    items = session.execute(statement).all()
    return items

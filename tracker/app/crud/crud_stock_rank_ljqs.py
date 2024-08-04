# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     crud_stock_rank_ljqs
   Description : 技术指标 -- 量价齐升
   Author :       EveryFine
   Date：          2024/7/22
-------------------------------------------------
   Change Activity:
                   2024/7/22:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

import datetime

import akshare as ak
from sqlmodel import Session, select

from app.common.log import log
from app.crud.crud_stock_trade_date import get_last_trade_date, get_last_trade_date_by_date
from app.models.stock_rank_ljqs import StockRankLjqs


def create_stock_rank_ljqs(*, session: Session) -> int:
    ljqs_count = 0
    trade_date = get_last_trade_date(session=session, final_datetime=datetime.datetime.now())
    stock_rank_ljqs_ths_df = ak.stock_rank_ljqs_ths()
    for index, row in stock_rank_ljqs_ths_df.iterrows():
        res = create_stock_rank_ljqs_item(session, trade_date, row)
        ljqs_count += res
        if ljqs_count > 0 and ljqs_count % 100 == 0:
            session.commit()
    session.commit()
    log.info(f'creat stock rank ljqs finish, created count: {ljqs_count}')
    return ljqs_count


def create_stock_rank_ljqs_item(session, trade_date, row):
    symbol = row['股票代码']
    name = row['股票简称']
    latest_price = row['最新价']
    qs_days = row['量价齐升天数']
    days_change_rate = row['阶段涨幅']
    turnover_rate = row['累计换手率']
    industry = row['所属行业']
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()

    items_saved = get_stock_rank_ljqs_items(session, symbol, trade_date)
    if items_saved is None or len(items_saved) == 0:
        stock_rank_ljqs_create = StockRankLjqs(trade_date=trade_date, symbol=symbol, name=name,
                                               latest_price=latest_price, qs_days=qs_days,
                                               days_change_rate=days_change_rate, turnover_rate=turnover_rate,
                                               industry=industry, created_at=created_at, updated_at=updated_at)
        db_stock_rank_ljqs = StockRankLjqs.model_validate(stock_rank_ljqs_create)
        session.add(db_stock_rank_ljqs)
        return 1
    else:
        return 0


def get_stock_rank_ljqs_items(session, symbol, trade_date):
    statement = (select(StockRankLjqs).where(StockRankLjqs.symbol == symbol).
                 where(StockRankLjqs.trade_date == trade_date))
    items = session.execute(statement).all()
    return items


def check_stock_rank_ljqs_date(session, check_date):
    last_trade_date = get_last_trade_date_by_date(session=session, final_date=check_date)
    statement = select(StockRankLjqs).where(
        StockRankLjqs.trade_date == last_trade_date)
    items = session.execute(statement).all()
    if items is None or len(items) == 0:
        return False
    else:
        return True

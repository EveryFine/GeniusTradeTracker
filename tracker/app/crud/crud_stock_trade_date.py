# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     crud_stock_trade_date
   Description :
   Author :       EveryFine
   Date：          2024/7/16
-------------------------------------------------
   Change Activity:
                   2024/7/16:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

import datetime

import akshare as ak
from sqlmodel import Session, select

from app.common.log import log
from app.models.stock_trade_date import StockTradeDate


def create_stock_trade_dates(*, session: Session) -> int:
    tool_trade_date_hist_sina_df = ak.tool_trade_date_hist_sina()
    trade_date_count = 0
    for index, row in tool_trade_date_hist_sina_df.iterrows():
        res = create_stock_trade_date_item(session=session, row=row)
        trade_date_count += res
    session.commit()
    log.info(f'creat stock trade dates finish, created count: {trade_date_count}')
    return trade_date_count


def create_stock_trade_date_item(session, row):
    trade_date = row['trade_date']
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()
    trade_date_saved = get_stock_trade_dates(session, trade_date)
    if trade_date_saved is None or len(trade_date_saved) == 0:
        stock_trade_date_create = StockTradeDate(trade_date=trade_date, created_at=created_at, updated_at=updated_at)
        db_stock_trade_date = StockTradeDate.model_validate(stock_trade_date_create)
        session.add(db_stock_trade_date)
        res = 1
        return res
    else:
        return 0


def get_stock_trade_dates(session, trade_date):
    statement = select(StockTradeDate).where(StockTradeDate.trade_date == trade_date)
    stock_trade_date_items = session.execute(statement).all()
    return stock_trade_date_items


def get_last_trade_date(session, date):
    statement = select(StockTradeDate).where(StockTradeDate.trade_date <= date).order_by(
        StockTradeDate.trade_date.desc())
    last_trade_date_item = session.execute(statement).first()
    return last_trade_date_item[0].trade_date

# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     crud_stock_history_hfq
   Description :
   Author :       EveryFine
   Date：          2024/7/14
-------------------------------------------------
   Change Activity:
                   2024/7/14:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

from datetime import timedelta

from fastapi import Query
from sqlmodel import Session, select
import akshare as ak
from app.crud.crud_stock_info import get_all_stocks, get_stock_infos
from app.crud.crud_stock_trade_date import get_last_trade_date, get_last_trade_date_by_date
from app.models.stock_history_hfq import StockHistoryHfq, StockHistoryHfqCreate


def create_stock_histories(*, session: Session) -> int:
    stock_infos = get_all_stocks(session=session)
    history_count = create_histories_by_list(session, stock_infos)
    return history_count


def create_histories_by_list(session, stock_infos):
    history_count = 0
    for stock_info in stock_infos:
        start_date = get_start_date(session=session, symbol=stock_info.symbol)
        end_date = 20500101
        stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol=stock_info.symbol, start_date=start_date, end_date=end_date,
                                                period="daily", adjust="hfq")
        for index, row in stock_zh_a_hist_df.iterrows():
            stock_hist = create_stock_hist(session=session, row=row)
            history_count += 1
        session.commit()
    return history_count


def create_part_stock_histories(*, session: Session, stock_offset: int = 0,
                                stock_limit: int = Query(default=1000, le=1000)) -> int:
    stock_infos_public = get_stock_infos(session=session, offset=stock_offset, limit=stock_limit)
    stock_infos = stock_infos_public.data
    history_count = create_histories_by_list(session, stock_infos)
    return history_count


def get_start_date(session, symbol) -> str:
    stock_hists = get_stock_histories(session, symbol)
    if stock_hists is None or len(stock_hists) == 0:
        return '19700101'
    stock_hist = stock_hists[0][0]
    last_date = stock_hist.date
    query_start_date = last_date + timedelta(days=1)
    start_date_str = query_start_date.strftime("%Y%m%d")
    return start_date_str


def get_stock_histories(session, symbol):
    statement = select(StockHistoryHfq).where(StockHistoryHfq.symbol == symbol).order_by(StockHistoryHfq.date.desc())
    stock_hists = session.execute(statement).all()
    return stock_hists


def create_stock_hist(session, row):
    symbol = row['股票代码']
    date = row['日期']
    open = row['开盘']
    close = row['收盘']
    high = row['最高']
    low = row['最低']
    volume = row['成交量']
    turnover = row['成交额']
    range = row['振幅']
    change_rate = row['涨跌幅']
    change_amount = row['涨跌额']
    turnover_rate = row['换手率']
    stock_hist_create = StockHistoryHfqCreate(symbol=symbol, date=date, open=open, close=close, high=high, low=low,
                                              volume=volume, turnover=turnover, range=range, change_rate=change_rate,
                                              change_amount=change_amount, turnover_rate=turnover_rate)
    db_stock_hist = StockHistoryHfq.model_validate(stock_hist_create)
    session.add(db_stock_hist)
    # session.commit()
    # session.refresh(db_stock_hist)
    res = StockHistoryHfq.model_validate(db_stock_hist)
    return res


def check_stock_history_hfq_date(session, check_date):
    last_trade_date = get_last_trade_date_by_date(session=session, final_date=check_date)
    statement = select(StockHistoryHfq).where(
        StockHistoryHfq.date == last_trade_date)
    items = session.execute(statement).all()
    if items is None or len(items) < 4000:
        return False
    else:
        return True

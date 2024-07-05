# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     crud_stock_history
   Description :
   Author :       EveryFine
   Date：          2024/7/4
-------------------------------------------------
   Change Activity:
                   2024/7/4:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

from typing import List

from sqlmodel import Session

import akshare as ak

from app.crud.crud_stock_info import get_all_stocks
from app.models.stock_history import StockHistory, StockHistoryCreate


def create_stock_histories(*, session: Session) -> int:
    history_count = 0
    stock_infos = get_all_stocks(session=session)
    for stock_info in stock_infos:
        stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol=stock_info.symbol, period="daily", adjust="")
        for index, row in stock_zh_a_hist_df.iterrows():
            stock_hist = create_stock_hist(session=session, row=row)

            history_count += 1

    return history_count


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
    stock_hist_create = StockHistoryCreate(symbol=symbol, date=date, open=open, close=close, high=high, low=low,
                                           volume=volume, turnover=turnover, range=range, change_rate=change_rate,
                                           change_amount=change_amount, turnover_rate=turnover_rate)
    db_stock_hist = StockHistory.model_validate(stock_hist_create)
    session.add(db_stock_hist)
    session.commit()
    session.refresh(db_stock_hist)
    res = StockHistory.model_validate(db_stock_hist)
    return res

# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     crud_stock_rank_lxxd
   Description :    技术指标 -- 连续下跌
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
from app.models.stock_rank_lxxd import StockRankLxxd


def create_stock_rank_lxxd(*, session: Session) -> int:
    lxxd_count = 0
    trade_date = get_last_trade_date(session=session, final_datetime=datetime.datetime.now())
    stock_rank_lxxd_ths_df = ak.stock_rank_lxxd_ths()
    for index, row in stock_rank_lxxd_ths_df.iterrows():
        res = create_stock_rank_lxxd_item(session, trade_date, row)
        lxxd_count += res
        if lxxd_count > 0 and lxxd_count % 100 == 0:
            session.commit()
    session.commit()
    log.info(f'creat stock rank lxxd finish, created count: {lxxd_count}')
    return lxxd_count


def create_stock_rank_lxxd_item(session, trade_date, row):
    symbol = row['股票代码']
    name = row['股票简称']
    close = row['收盘价']
    high = row['最高价']
    low = row['最低价']
    lz_days = row['连涨天数']
    lz_change_rate = row['连续涨跌幅']
    turnover_rate = row['累计换手率']
    industry = row['所属行业']
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()

    items_saved = get_stock_rank_lxxd_items(session, symbol, trade_date)
    if items_saved is None or len(items_saved) == 0:
        stock_rank_lxxd_create = StockRankLxxd(trade_date=trade_date, symbol=symbol, name=name, close=close, high=high,
                                               low=low, lz_days=lz_days, lz_change_rate=lz_change_rate,
                                               turnover_rate=turnover_rate, industry=industry, created_at=created_at,
                                               updated_at=updated_at)
        db_stock_rank_lxxd = StockRankLxxd.model_validate(stock_rank_lxxd_create)
        session.add(db_stock_rank_lxxd)
        return 1
    else:
        return 0


def get_stock_rank_lxxd_items(session, symbol, trade_date):
    statement = (select(StockRankLxxd).where(StockRankLxxd.symbol == symbol).
                 where(StockRankLxxd.trade_date == trade_date))
    items = session.execute(statement).all()
    return items
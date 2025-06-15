# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_lhb_hyyyb_em
   Description :
   Author :       EveryFine
   Date：          2025/6/15
-------------------------------------------------
   Change Activity:
                   2025/6/15:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

import datetime

import akshare as ak
from sqlalchemy import func
from sqlmodel import Session, select

from app.models.stock_lhb_hyyyb_em import StockLhbHyyybEm, StockLhbHyyybEmCreate


def create_stock_lhb_hyyyb_em(*, session: Session) -> int:
    start_date = get_start_date(session=session)
    end_date = '20500101'
    # end_date = '20150725'
    count = 0
    stock_lhb_hyyyb_em_df = ak.stock_lhb_hyyyb_em(start_date=start_date, end_date=end_date)
    for index, row in stock_lhb_hyyyb_em_df.iterrows():
        stock_lhb_hyyyb_item = create_stock_lhb_hyyyb_em_item(session=session, row=row)
        count += 1
        if count % 100 == 0:
            session.commit()
    session.commit()

    return count


def get_start_date(session) -> str:
    trade_date_latest = get_trade_date_latest(session)
    if trade_date_latest is None:
        return '20040525'
        # return '20250601'

    query_start_date = trade_date_latest + datetime.timedelta(days=1)
    start_date_str = query_start_date.strftime("%Y%m%d")
    return start_date_str


def get_trade_date_latest(session):
    statement = select(func.max(StockLhbHyyybEm.trade_date))
    max_trade_date = session.execute(statement).scalar_one()
    return max_trade_date


def create_stock_lhb_hyyyb_em_item(session, row):
    yyb_symbol = row['营业部代码']
    yyb_name = row['营业部名称']
    trade_date = row['上榜日']

    buy_stock_count = row['买入个股数']
    sell_stock_count = row['卖出个股数']
    buy_amount_total = row['买入总金额']
    sell_amount_total = row['卖出总金额']
    net_amount_total = row['总买卖净额']
    buy_stocks = row['买入股票']

    stock_lhb_hyyyb_em_create = StockLhbHyyybEmCreate(yyb_symbol=yyb_symbol,
                                                      yyb_name=yyb_name,
                                                      trade_date=trade_date,
                                                      buy_stock_count=buy_stock_count,
                                                      sell_stock_count=sell_stock_count,
                                                      buy_amount_total=buy_amount_total,
                                                      sell_amount_total=sell_amount_total,
                                                      net_amount_total=net_amount_total,
                                                      buy_stocks=buy_stocks)
    db_stock_lhb_hyyyb_em = StockLhbHyyybEm.model_validate(stock_lhb_hyyyb_em_create)
    session.add(db_stock_lhb_hyyyb_em)
    res = StockLhbHyyybEm.model_validate(db_stock_lhb_hyyyb_em)
    return res

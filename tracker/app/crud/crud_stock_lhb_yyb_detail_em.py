# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     crud_stock_lhb_yyb_detail_em
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

from app.models.stock_lhb_hyyyb_em import StockLhbHyyybEm
from app.models.stock_lhb_yyb_detail_em import StockLhbYybDetailEm, StockLhbYybDetailEmCreate


def create_stock_lhb_yyb_detail_em(*, session: Session) -> int:
    yyb_list = get_yyb_list(session=session)
    count = create_stock_lhb_yyb_detail_em_by_list(session, yyb_list)
    return count


def create_stock_lhb_yyb_detail_em_by_list(session, yyb_list):
    detail_count = 0
    for yyb_symbol in yyb_list:

        stock_lhb_yyb_detail_em_df = ak.stock_lhb_yyb_detail_em(symbol=yyb_symbol)

        for index, row in stock_lhb_yyb_detail_em_df.iterrows():
            detail_item_res = create_yyb_detail_item(session=session, row=row)
            detail_count += detail_item_res
        session.commit()

    return detail_count


def get_yyb_list(session):
    statement = select(StockLhbHyyybEm.yyb_symbol).distinct()
    result = session.execute(statement).scalars().all()
    return result


def create_yyb_detail_item(session, row):
    yyb_symbol = row['营业部代码']
    yyb_name = row['营业部名称']
    yyb_short_name = row['营业部简称']
    trade_date = row['交易日期']

    stock_symbol = row['股票代码']
    stock_name = row['股票名称']
    change_rate = row['涨跌幅']
    buy_amount = row['买入金额']
    sell_amount = row['卖出金额']
    net_amount = row['净额']

    reason = row['上榜原因']

    items_saved = get_yyb_detail_items(session, yyb_symbol, trade_date, stock_symbol)
    if items_saved is None or len(items_saved) == 0:
        stock_lhb_yyb_detail_em_create = StockLhbYybDetailEmCreate(yyb_symbol=yyb_symbol,
                                                                   yyb_name=yyb_name,
                                                                   yyb_short_name=yyb_short_name,
                                                                   trade_date=trade_date,
                                                                   stock_symbol=stock_symbol,
                                                                   stock_name=stock_name,
                                                                   change_rate=change_rate,
                                                                   buy_amount=buy_amount,
                                                                   sell_amount=sell_amount,
                                                                   net_amount=net_amount,
                                                                   reason=reason)
        db_stock_lhb_yyb_detail_em = StockLhbYybDetailEm.model_validate(stock_lhb_yyb_detail_em_create)
        session.add(db_stock_lhb_yyb_detail_em)
        res = StockLhbYybDetailEm.model_validate(db_stock_lhb_yyb_detail_em)
        return 1
    else:
        return 0


def get_yyb_detail_items(session, yyb_symbol, trade_date, stock_symbol):
    statement = (select(StockLhbYybDetailEm).where(StockLhbYybDetailEm.yyb_symbol == yyb_symbol).where(
        StockLhbYybDetailEm.trade_date == trade_date).where(
        StockLhbYybDetailEm.stock_symbol == stock_symbol))
    items = session.execute(statement).all()
    return items

# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     crud_stock_fund_big_deal
   Description :    资金流 -- 大单追踪
   Author :       EveryFine
   Date：          2024/7/27
-------------------------------------------------
   Change Activity:
                   2024/7/27:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

import datetime
from decimal import Decimal

import akshare as ak
from sqlmodel import Session, select

from app.common.log import log
from app.crud.crud_stock_fund_single_intraday import per_str_to_float
from app.crud.crud_stock_trade_date import get_last_trade_date, get_last_trade_date_by_date
from app.models.stock_fund_big_deal import StockFundBigDeal


def create_stock_fund_big_deal(*, session: Session) -> int:
    total_count = 0
    trade_date = get_last_trade_date(session=session, final_datetime=datetime.datetime.now())
    stock_fund_big_deal_ths_df = ak.stock_fund_flow_big_deal()
    for index, row in stock_fund_big_deal_ths_df.iterrows():
        res = create_stock_fund_big_deal_item(session, trade_date, row)
        total_count += res
        if total_count > 0 and total_count % 100 == 0:
            session.commit()
    session.commit()
    log.info(f'creat stock fund big deal(资金流--大单追踪) finish, created count: {total_count}')
    return total_count


def create_stock_fund_big_deal_item(session, trade_date, row):
    trade_time = row['成交时间']
    symbol = f"{row['股票代码']:06d}"
    name = row['股票简称']
    price = row['成交价格']
    volume = row['成交量']
    turnover = row['成交额']
    type = row['大单性质']
    change_rate = per_str_to_float(row['涨跌幅'])
    change_amount = row['涨跌额']
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()

    items_saved = get_stock_fund_big_deal_items(session, symbol, trade_time, volume, price)
    if items_saved is None or len(items_saved) == 0:
        stock_fund_big_deal_create = StockFundBigDeal(trade_date=trade_date,
                                                      trade_time=trade_time,
                                                      symbol=symbol,
                                                      name=name,
                                                      price=price,
                                                      volume=volume,
                                                      turnover=turnover,
                                                      type=type,
                                                      change_rate=change_rate,
                                                      change_amount=change_amount,
                                                      created_at=created_at,
                                                      updated_at=updated_at)
        db_stock_fund_big_deal = StockFundBigDeal.model_validate(stock_fund_big_deal_create)
        session.add(db_stock_fund_big_deal)
        return 1
    else:
        return 0


def get_stock_fund_big_deal_items(session, symbol, trade_time, volume, price):
    statement = (select(StockFundBigDeal).where(StockFundBigDeal.symbol == symbol).
                 where(StockFundBigDeal.trade_time == trade_time).where(StockFundBigDeal.volume == volume).
                 where(StockFundBigDeal.price == price))
    items = session.execute(statement).all()
    return items


def check_stock_fund_big_deal_date(session, check_date):
    last_trade_date = get_last_trade_date_by_date(session=session, final_date=check_date)
    statement = select(StockFundBigDeal).where(
        StockFundBigDeal.trade_date == last_trade_date)
    items = session.execute(statement).all()
    if items is None or len(items) == 0:
        return False
    else:
        return True

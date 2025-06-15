# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     crud_stock_lhb_detail_em
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
from typing import List
import time

from fastapi import Query
from sqlmodel import Session, select
from sqlalchemy import func

import akshare as ak

from app.common.log import log
from app.crud.crud_stock_info import get_all_stocks, get_stock_infos
from app.crud.crud_stock_trade_date import get_last_trade_date, get_last_trade_date_by_date
from app.models.stock_lhb_detail_em import StockLhbDetailEm, StockLhbDetailEmCreate


def create_stock_lhb_detail_em(*, session: Session) -> int:
    start_date = get_start_date(session=session)
    end_date = '20500101'
    count = 0
    stock_lhb_detail_em_df = ak.stock_lhb_detail_em(start_date=start_date, end_date=end_date)
    for index, row in stock_lhb_detail_em_df.iterrows():
        stock_lhb_item = create_stock_lhb_detail_em_item(session=session, row=row)
        count += 1
        if count % 100 == 0:
            session.commit()
    session.commit()

    return count


def get_start_date(session) -> str:
    trade_date_latest = get_trade_date_latest(session)
    if trade_date_latest is None:
        return '19700101'
        # return '20250601'

    query_start_date = trade_date_latest + datetime.timedelta(days=1)
    start_date_str = query_start_date.strftime("%Y%m%d")
    return start_date_str


def get_trade_date_latest(session):
    statement = select(func.max(StockLhbDetailEm.trade_date))
    max_trade_date = session.execute(statement).scalar_one()
    return max_trade_date


def create_stock_lhb_detail_em_item(session, row):
    trade_date = row['上榜日']
    name = row['名称']
    symbol = row['代码']
    insight = row['解读']
    close = row['收盘价']
    change_rate = row['涨跌幅']
    lhb_in_net = row['龙虎榜净买额']
    lhb_in_amount = row['龙虎榜买入额']
    lhb_out_amount = row['龙虎榜卖出额']
    lhb_amount = row['龙虎榜成交额']
    total_amount = row['市场总成交额']
    in_net_per = row['净买额占总成交比']
    in_amount_per = row['成交额占总成交比']

    turnover_rate = row['换手率']
    traded_market_value = row['流通市值']
    reason = row['上榜原因']

    stock_lhb_detail_em_create = StockLhbDetailEmCreate(trade_date=trade_date,
                                                        name=name,
                                                        symbol=symbol,
                                                        insight=insight,
                                                        close=close,
                                                        change_rate=change_rate,
                                                        lhb_in_net=lhb_in_net,
                                                        lhb_in_amount=lhb_in_amount,
                                                        lhb_out_amount=lhb_out_amount,
                                                        lhb_amount=lhb_amount,
                                                        total_amount=total_amount,
                                                        in_net_per=in_net_per,
                                                        in_amount_per=in_amount_per,
                                                        turnover_rate=turnover_rate,
                                                        traded_market_value=traded_market_value,
                                                        reason=reason
                                                        )
    db_stock_lhb_detail_em = StockLhbDetailEm.model_validate(stock_lhb_detail_em_create)
    session.add(db_stock_lhb_detail_em)
    res = StockLhbDetailEm.model_validate(db_stock_lhb_detail_em)
    return res

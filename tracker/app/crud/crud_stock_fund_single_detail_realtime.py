# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     crud_stock_fund_single_detail_realtime
   Description :
   Author :       EveryFine
   Date：          2025/6/19
-------------------------------------------------
   Change Activity:
                   2025/6/19:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

import datetime
import pandas as pd

import akshare as ak
from sqlmodel import Session, select

from app.common.log import log
from app.crud.crud_stock_trade_date import get_last_trade_date, get_last_trade_date_by_date
from app.models.stock_fund_single_detail_realtime import StockFundSingleDetailRealtime


def create_stock_fund_single_detail_realtime(*, session: Session) -> int:
    total_count = 0
    trade_date = datetime.date.today()
    stock_fund_single_detail_realtime_ths_df = ak.stock_individual_fund_flow_rank(indicator="今日")
    # 强制转换为数值，无法转换的变为NaN
    stock_fund_single_detail_realtime_ths_df['今日主力净流入-净占比'] = pd.to_numeric(
        stock_fund_single_detail_realtime_ths_df['今日主力净流入-净占比'], errors='coerce'
    )
    # 去除NaN
    filtered_df = stock_fund_single_detail_realtime_ths_df.dropna(subset=['今日主力净流入-净占比'])

    filtered_df = filtered_df[
        (filtered_df['今日主力净流入-净额'] > 5000000) &
        (filtered_df['今日主力净流入-净占比'] > 0)
        ]

    top30 = filtered_df.sort_values(by='今日主力净流入-净占比', ascending=False).head(30)
    for index, row in top30.iterrows():
        res = create_stock_fund_single_detail_realtime_item(session, trade_date, row)
        total_count += res
        if total_count > 0 and total_count % 100 == 0:
            session.commit()
    session.commit()
    log.info(f'creat stock fund single detail realtime(个股资金流详细--实时) finish, created count: {total_count}')
    return total_count


def create_stock_fund_single_detail_realtime_item(session, trade_date, row):
    symbol = row['代码']
    name = row['名称']
    latest_price = get_value_with_hyphen(row['最新价'])
    change_rate = get_value_with_hyphen(row['今日涨跌幅'])

    main_in_rank = row['序号']
    main_in_net = get_value_with_hyphen(row['今日主力净流入-净额'])
    main_in_per = get_value_with_hyphen(row['今日主力净流入-净占比'])

    huge_in_net = get_value_with_hyphen(row['今日超大单净流入-净额'])
    huge_in_per = get_value_with_hyphen(row['今日超大单净流入-净占比'])

    big_in_net = get_value_with_hyphen(row['今日大单净流入-净额'])
    big_in_per = get_value_with_hyphen(row['今日大单净流入-净占比'])

    middle_in_net = get_value_with_hyphen(row['今日中单净流入-净额'])
    middle_in_per = get_value_with_hyphen(row['今日中单净流入-净占比'])

    small_in_net = get_value_with_hyphen(row['今日小单净流入-净额'])
    small_in_per = get_value_with_hyphen(row['今日小单净流入-净占比'])

    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()

    stock_fund_single_detail_realtime_create = StockFundSingleDetailRealtime(trade_date=trade_date,
                                                                             symbol=symbol,
                                                                             name=name,
                                                                             latest_price=latest_price,
                                                                             change_rate=change_rate,
                                                                             main_in_rank=main_in_rank,
                                                                             main_in_net=main_in_net,
                                                                             main_in_per=main_in_per,
                                                                             huge_in_net=huge_in_net,
                                                                             huge_in_per=huge_in_per,
                                                                             big_in_net=big_in_net,
                                                                             big_in_per=big_in_per,
                                                                             middle_in_net=middle_in_net,
                                                                             middle_in_per=middle_in_per,
                                                                             small_in_net=small_in_net,
                                                                             small_in_per=small_in_per,
                                                                             created_at=created_at,
                                                                             updated_at=updated_at)
    db_stock_fund_single_detail_realtime = StockFundSingleDetailRealtime.model_validate(
        stock_fund_single_detail_realtime_create)
    session.add(db_stock_fund_single_detail_realtime)
    return 1


def get_value_with_hyphen(param):
    if param is None:
        return None
    elif str(param) == '-':
        return None
    else:
        return param


def check_stock_fund_single_detail_realtime_date(session, check_date):
    last_trade_date = get_last_trade_date_by_date(session=session, final_date=check_date)
    statement = select(StockFundSingleDetailRealtime).where(
        StockFundSingleDetailRealtime.trade_date == last_trade_date)
    items = session.execute(statement).all()
    if items is None or len(items) == 0:
        return False
    else:
        return True

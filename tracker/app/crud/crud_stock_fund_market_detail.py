# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     crud_stock_fund_market_detail
   Description :  资金流--大盘
   Author :       EveryFine
   Date：          2024/7/28
-------------------------------------------------
   Change Activity:
                   2024/7/28:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

import datetime

import akshare as ak
from sqlmodel import Session, select

from app.common.log import log
from app.crud.crud_stock_fund_single_detail_intraday import get_value_with_hyphen
from app.crud.crud_stock_trade_date import get_last_trade_date
from app.models.stock_fund_market_detail import StockFundMarketDetail


def create_stock_fund_market_detail(*, session: Session) -> int:
    total_count = 0
    stock_fund_market_detail_ths_df = ak.stock_market_fund_flow()
    for index, row in stock_fund_market_detail_ths_df.iterrows():
        res = create_stock_fund_market_detail_item(session, row)
        total_count += res
        if total_count > 0 and total_count % 100 == 0:
            session.commit()
    session.commit()
    log.info(f'creat stock fund market detail(资金流--大盘) finish, created count: {total_count}')
    return total_count


def create_stock_fund_market_detail_item(session, row):
    trade_date = row['日期']

    sh_close = get_value_with_hyphen(row['上证-收盘价'])
    sh_change_rate = get_value_with_hyphen(row['上证-涨跌幅'])

    sz_close = get_value_with_hyphen(row['深证-收盘价'])
    sz_change_rate = get_value_with_hyphen(row['深证-涨跌幅'])

    main_in_net = get_value_with_hyphen(row['主力净流入-净额'])
    main_in_per = get_value_with_hyphen(row['主力净流入-净占比'])

    huge_in_net = get_value_with_hyphen(row['超大单净流入-净额'])
    huge_in_per = get_value_with_hyphen(row['超大单净流入-净占比'])

    big_in_net = get_value_with_hyphen(row['大单净流入-净额'])
    big_in_per = get_value_with_hyphen(row['大单净流入-净占比'])

    middle_in_net = get_value_with_hyphen(row['中单净流入-净额'])
    middle_in_per = get_value_with_hyphen(row['中单净流入-净占比'])

    small_in_net = get_value_with_hyphen(row['小单净流入-净额'])
    small_in_per = get_value_with_hyphen(row['小单净流入-净占比'])

    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()

    items_saved = get_stock_fund_market_detail_items(session, trade_date)
    if items_saved is None or len(items_saved) == 0:
        stock_fund_market_detail_create = StockFundMarketDetail(trade_date=trade_date,
                                                                sh_close=sh_close,
                                                                sh_change_rate=sh_change_rate,
                                                                sz_close=sz_close,
                                                                sz_change_rate=sz_change_rate,
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
        db_stock_fund_market_detail = StockFundMarketDetail.model_validate(stock_fund_market_detail_create)
        session.add(db_stock_fund_market_detail)
        return 1
    else:
        return 0


def get_stock_fund_market_detail_items(session, trade_date):
    statement = (select(StockFundMarketDetail).
                 where(StockFundMarketDetail.trade_date == trade_date))
    items = session.execute(statement).all()
    return items

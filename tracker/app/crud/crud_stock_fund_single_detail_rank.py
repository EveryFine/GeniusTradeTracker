# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     crud_stock_fund_single_detail_rank
   Description :   资金流--个股--详细--排名
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
from app.crud.crud_stock_trade_date import get_last_trade_date, get_last_trade_date_by_date
from app.models.stock_fund_single_detail_rank import StockFundSingleDetailRank


def create_stock_fund_single_detail_rank(*, session: Session) -> int:
    range_types = (
        "3日", "5日", "10日")
    total_count = create_stock_fund_single_detail_rank_by_types(session, range_types)
    return total_count


def create_stock_fund_single_detail_rank_by_types(session, range_types):
    total_count = 0
    for range_type in range_types:
        res = create_stock_fund_single_detail_rank_by_type(session, range_type)
        total_count += res
        session.commit()
        log.info(
            f'creat stock fund single detail rank(个股资金流--详细--排行) by range type finish, type:{range_type}, created count: {res}')
    session.commit()
    log.info(f'creat stock fund single detail rank(个股资金流--详细--排行) finish, total count: {total_count}')
    return total_count


def create_stock_fund_single_detail_rank_by_type(session, range_type) -> int:
    type_count = 0
    trade_date = get_last_trade_date(session=session, final_datetime=datetime.datetime.now())
    stock_fund_single_detail_rank_ths_df = ak.stock_individual_fund_flow_rank(indicator=range_type)
    for index, row in stock_fund_single_detail_rank_ths_df.iterrows():
        res = create_stock_fund_single_detail_rank_item(session, trade_date, row, range_type)
        type_count += res
        if type_count > 0 and type_count % 100 == 0:
            session.commit()
    session.commit()
    return type_count


def create_stock_fund_single_detail_rank_item(session, trade_date, row, range_type):
    symbol = row['代码']
    name = row['名称']
    latest_price = get_value_with_hyphen(row['最新价'])
    main_in_rank = row['序号']
    if range_type == '3日':
        change_rate = get_value_with_hyphen(row['3日涨跌幅'])
        main_in_net = get_value_with_hyphen(row['3日主力净流入-净额'])
        main_in_per = get_value_with_hyphen(row['3日主力净流入-净占比'])

        huge_in_net = get_value_with_hyphen(row['3日超大单净流入-净额'])
        huge_in_per = get_value_with_hyphen(row['3日超大单净流入-净占比'])

        big_in_net = get_value_with_hyphen(row['3日大单净流入-净额'])
        big_in_per = get_value_with_hyphen(row['3日大单净流入-净占比'])

        middle_in_net = get_value_with_hyphen(row['3日中单净流入-净额'])
        middle_in_per = get_value_with_hyphen(row['3日中单净流入-净占比'])

        small_in_net = get_value_with_hyphen(row['3日小单净流入-净额'])
        small_in_per = get_value_with_hyphen(row['3日小单净流入-净占比'])
    if range_type == '5日':
        change_rate = get_value_with_hyphen(row['5日涨跌幅'])
        main_in_net = get_value_with_hyphen(row['5日主力净流入-净额'])
        main_in_per = get_value_with_hyphen(row['5日主力净流入-净占比'])

        huge_in_net = get_value_with_hyphen(row['5日超大单净流入-净额'])
        huge_in_per = get_value_with_hyphen(row['5日超大单净流入-净占比'])

        big_in_net = get_value_with_hyphen(row['5日大单净流入-净额'])
        big_in_per = get_value_with_hyphen(row['5日大单净流入-净占比'])

        middle_in_net = get_value_with_hyphen(row['5日中单净流入-净额'])
        middle_in_per = get_value_with_hyphen(row['5日中单净流入-净占比'])

        small_in_net = get_value_with_hyphen(row['5日小单净流入-净额'])
        small_in_per = get_value_with_hyphen(row['5日小单净流入-净占比'])
    if range_type == '10日':
        change_rate = get_value_with_hyphen(row['10日涨跌幅'])
        main_in_net = get_value_with_hyphen(row['10日主力净流入-净额'])
        main_in_per = get_value_with_hyphen(row['10日主力净流入-净占比'])

        huge_in_net = get_value_with_hyphen(row['10日超大单净流入-净额'])
        huge_in_per = get_value_with_hyphen(row['10日超大单净流入-净占比'])

        big_in_net = get_value_with_hyphen(row['10日大单净流入-净额'])
        big_in_per = get_value_with_hyphen(row['10日大单净流入-净占比'])

        middle_in_net = get_value_with_hyphen(row['10日中单净流入-净额'])
        middle_in_per = get_value_with_hyphen(row['10日中单净流入-净占比'])

        small_in_net = get_value_with_hyphen(row['10日小单净流入-净额'])
        small_in_per = get_value_with_hyphen(row['10日小单净流入-净占比'])

    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()

    items_saved = get_stock_fund_single_detail_rank_items(session, symbol, trade_date, range_type)
    if items_saved is None or len(items_saved) == 0:
        stock_fund_single_detail_intraday_create = StockFundSingleDetailRank(trade_date=trade_date,
                                                                             range_type=range_type,
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
        db_stock_fund_single_detail_intraday = StockFundSingleDetailRank.model_validate(
            stock_fund_single_detail_intraday_create)
        session.add(db_stock_fund_single_detail_intraday)
        return 1
    else:
        return 0


def get_stock_fund_single_detail_rank_items(session, symbol, trade_date, range_type):
    statement = (select(StockFundSingleDetailRank).where(StockFundSingleDetailRank.symbol == symbol).where(
        StockFundSingleDetailRank.trade_date == trade_date).where(
        StockFundSingleDetailRank.range_type == range_type))
    items = session.execute(statement).all()
    return items

def check_stock_fund_single_detail_rank_date(session, check_date):
    last_trade_date = get_last_trade_date_by_date(session=session, final_date=check_date)
    statement = select(StockFundSingleDetailRank).where(
        StockFundSingleDetailRank.trade_date == last_trade_date)
    items = session.execute(statement).all()
    if items is None or len(items) == 0:
        return False
    else:
        return True



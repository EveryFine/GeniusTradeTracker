# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     crud_stock_fund_single_rank
   Description :
   Author :       EveryFine
   Date：          2024/7/26
-------------------------------------------------
   Change Activity:
                   2024/7/26:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

import datetime

import akshare as ak
from sqlmodel import Session, select

from app.common.log import log
from app.crud.crud_stock_fund_single_intraday import per_str_to_float, fund_str_to_float
from app.crud.crud_stock_trade_date import get_last_trade_date
from app.models.stock_fund_single_rank import StockFundSingleRank


def create_stock_fund_single_ranks(*, session: Session) -> int:
    range_types = (
        "3日排行", "5日排行", "10日排行", "20日排行")
    total_count = create_stock_fund_single_rank_by_types(session, range_types)
    return total_count


def create_stock_fund_single_rank_by_types(session, range_types):
    total_count = 0
    for range_type in range_types:
        res = create_stock_fund_single_rank_by_type(session, range_type)
        total_count += res
        session.commit()
        log.info(
            f'creat stock fund single rank(个股资金流--排行) by range type finish, type:{range_type}, created count: {res}')
    session.commit()
    log.info(f'creat stock fund single rank finish, total count: {total_count}')
    return total_count


def create_stock_fund_single_rank_by_type(session, range_type) -> int:
    type_count = 0
    trade_date = get_last_trade_date(session=session, final_datetime=datetime.datetime.now())
    stock_fund_single_rank_ths_df = ak.stock_fund_flow_individual(symbol=range_type)
    for index, row in stock_fund_single_rank_ths_df.iterrows():
        res = create_stock_fund_single_rank_item(session, trade_date, row, range_type)
        type_count += res
        if type_count > 0 and type_count % 100 == 0:
            session.commit()
    session.commit()
    return type_count


def create_stock_fund_single_rank_item(session, trade_date, row, range_type):
    symbol = f"{row['股票代码']:06d}"
    name = row['股票简称']
    latest_price = row['最新价']
    change_rate = per_str_to_float(row['阶段涨跌幅'])
    change_rate_rank = row['序号']
    turnover_rate = per_str_to_float(row['连续换手率'])
    fund_in_net = fund_str_to_float(row['资金流入净额'])
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()

    items_saved = get_stock_fund_single_rank_items(session, symbol, trade_date, range_type)
    if items_saved is None or len(items_saved) == 0:
        stock_fund_single_rank_create = StockFundSingleRank(trade_date=trade_date, range_type=range_type, symbol=symbol,
                                                            name=name,
                                                            latest_price=latest_price, change_rate=change_rate,
                                                            change_rate_rank=change_rate_rank,
                                                            turnover_rate=turnover_rate,
                                                            fund_in_net=fund_in_net, created_at=created_at,
                                                            updated_at=updated_at)
        db_stock_fund_single_rank = StockFundSingleRank.model_validate(stock_fund_single_rank_create)
        session.add(db_stock_fund_single_rank)
        return 1
    else:
        return 0


def get_stock_fund_single_rank_items(session, symbol, trade_date, range_type):
    statement = (select(StockFundSingleRank).where(StockFundSingleRank.symbol == symbol).where(StockFundSingleRank.trade_date == trade_date).where(
        StockFundSingleRank.range_type == range_type))
    items = session.execute(statement).all()
    return items

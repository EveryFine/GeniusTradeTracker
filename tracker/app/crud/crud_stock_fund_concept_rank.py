# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     crud_stock_fund_concept_rank
   Description :  资金流 -- 概念 -- 排名
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

import akshare as ak
from sqlmodel import Session, select

from app.common.log import log
from app.crud.crud_stock_fund_single_intraday import per_str_to_float
from app.crud.crud_stock_trade_date import get_last_trade_date, get_last_trade_date_by_date
from app.models.stock_fund_concept_rank import StockFundConceptRank


def create_stock_fund_concept_ranks(*, session: Session) -> int:
    range_types = (
        "3日排行", "5日排行", "10日排行", "20日排行")
    total_count = create_stock_fund_concept_rank_by_types(session, range_types)
    return total_count


def create_stock_fund_concept_rank_by_types(session, range_types):
    total_count = 0
    for range_type in range_types:
        res = create_stock_fund_concept_rank_by_type(session, range_type)
        total_count += res
        session.commit()
        log.info(
            f'creat stock fund concept rank(概念资金流--排行) by range type finish, type:{range_type}, created count: {res}')
    session.commit()
    log.info(f'creat stock fund concept rank(概念资金流--排行) finish, total count: {total_count}')
    return total_count


def create_stock_fund_concept_rank_by_type(session, range_type) -> int:
    type_count = 0
    trade_date = get_last_trade_date(session=session, final_datetime=datetime.datetime.now())
    stock_fund_concept_rank_ths_df = ak.stock_fund_flow_concept(symbol=range_type)
    for index, row in stock_fund_concept_rank_ths_df.iterrows():
        res = create_stock_fund_concept_rank_item(session, trade_date, row, range_type)
        type_count += res
        if type_count > 0 and type_count % 100 == 0:
            session.commit()
    session.commit()
    return type_count


def create_stock_fund_concept_rank_item(session, trade_date, row, range_type):
    name = row['行业']
    firm_number = row['公司家数']
    index = row['行业指数']
    change_rate = per_str_to_float(row['阶段涨跌幅'])
    change_rate_rank = row['序号']
    fund_in = row['流入资金']
    fund_out = row['流出资金']
    net_amount = row['净额']
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()

    items_saved = get_stock_fund_concept_rank_items(session, name, trade_date, range_type)
    if items_saved is None or len(items_saved) == 0:
        stock_fund_concept_rank_create = StockFundConceptRank(trade_date=trade_date,
                                                              range_type=range_type,
                                                              name=name,
                                                              firm_number=firm_number,
                                                              index=index,
                                                              change_rate=change_rate,
                                                              change_rate_rank=change_rate_rank,
                                                              fund_in=fund_in,
                                                              fund_out=fund_out,
                                                              net_amount=net_amount,
                                                              created_at=created_at,
                                                              updated_at=updated_at)
        db_stock_fund_concept_rank = StockFundConceptRank.model_validate(stock_fund_concept_rank_create)
        session.add(db_stock_fund_concept_rank)
        return 1
    else:
        return 0


def get_stock_fund_concept_rank_items(session, name, trade_date, range_type):
    statement = (select(StockFundConceptRank).where(StockFundConceptRank.name == name).where(
        StockFundConceptRank.trade_date == trade_date).where(
        StockFundConceptRank.range_type == range_type))
    items = session.execute(statement).all()
    return items


def check_stock_fund_concept_rank_date(session, check_date):
    last_trade_date = get_last_trade_date_by_date(session=session, final_date=check_date)
    statement = select(StockFundConceptRank).where(
        StockFundConceptRank.trade_date == last_trade_date)
    items = session.execute(statement).all()
    if items is None or len(items) == 0:
        return False
    else:
        return True

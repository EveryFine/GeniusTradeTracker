# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     crud_stock_fund_concept_detail_intraday
   Description :  资金流--概念--详细--即时
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
from app.models.stock_fund_concept_detail_intraday import StockFundConceptDetailIntraday


def create_stock_fund_concept_detail_intraday(*, session: Session) -> int:
    total_count = 0
    trade_date = get_last_trade_date(session=session, final_datetime=datetime.datetime.now())
    stock_fund_concept_detail_intraday_ths_df = ak.stock_sector_fund_flow_rank(indicator="今日",
                                                                               sector_type="概念资金流")
    for index, row in stock_fund_concept_detail_intraday_ths_df.iterrows():
        res = create_stock_fund_concept_detail_intraday_item(session, trade_date, row)
        total_count += res
        if total_count > 0 and total_count % 100 == 0:
            session.commit()
    session.commit()
    log.info(
        f'creat stock fund concept detail intraday(资金流--概念--详细--即时) finish, created count: {total_count}')
    return total_count


def create_stock_fund_concept_detail_intraday_item(session, trade_date, row):
    name = row['名称']
    change_rate = get_value_with_hyphen(row['今日涨跌幅'])

    main_in_rank = row['序号']
    main_in_net = get_value_with_hyphen(row['今日主力净流入-净额'])
    main_in_per = get_value_with_hyphen(row['今日主力净流入-净占比'])
    main_in_most_stock = row['今日主力净流入最大股']

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

    items_saved = get_stock_fund_concept_detail_intraday_items(session, name, trade_date)
    if items_saved is None or len(items_saved) == 0:
        stock_fund_concept_detail_intraday_create = StockFundConceptDetailIntraday(trade_date=trade_date,
                                                                                   name=name,
                                                                                   change_rate=change_rate,
                                                                                   main_in_rank=main_in_rank,
                                                                                   main_in_net=main_in_net,
                                                                                   main_in_per=main_in_per,
                                                                                   main_in_most_stock=main_in_most_stock,
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
        db_stock_fund_concept_detail_intraday = StockFundConceptDetailIntraday.model_validate(
            stock_fund_concept_detail_intraday_create)
        session.add(db_stock_fund_concept_detail_intraday)
        return 1
    else:
        return 0


def get_stock_fund_concept_detail_intraday_items(session, name, trade_date):
    statement = (select(StockFundConceptDetailIntraday).where(StockFundConceptDetailIntraday.name == name).
                 where(StockFundConceptDetailIntraday.trade_date == trade_date))
    items = session.execute(statement).all()
    return items

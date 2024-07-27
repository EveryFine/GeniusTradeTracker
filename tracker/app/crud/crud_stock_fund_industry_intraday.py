# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     crud_stock_fund_industry_intraday
   Description :    资金流 -- 行业 -- 即时
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
from app.crud.crud_stock_trade_date import get_last_trade_date
from app.models.stock_fund_industry_intraday import StockFundIndustryIntraday


def create_stock_fund_industry_intraday(*, session: Session) -> int:
    total_count = 0
    trade_date = get_last_trade_date(session=session, final_datetime=datetime.datetime.now())
    stock_fund_industry_intraday_ths_df = ak.stock_fund_flow_industry(symbol="即时")
    for index, row in stock_fund_industry_intraday_ths_df.iterrows():
        res = create_stock_fund_industry_intraday_item(session, trade_date, row)
        total_count += res
        if total_count > 0 and total_count % 100 == 0:
            session.commit()
    session.commit()
    log.info(f'creat stock fund industry intraday(行业资金流--即时) finish, created count: {total_count}')
    return total_count


def create_stock_fund_industry_intraday_item(session, trade_date, row):
    name = row['行业']
    index = row['行业指数']
    change_rate = row['行业-涨跌幅']
    change_rate_rank = row['序号']
    fund_in = row['流入资金']
    fund_out = row['流出资金']
    net_amount = row['净额']
    firm_number = row['公司家数']
    best_stock = row['领涨股']
    best_change_rate = row['领涨股-涨跌幅']
    best_latest_price = row['当前价']
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()

    items_saved = get_stock_fund_industry_intraday_items(session, name, trade_date)
    if items_saved is None or len(items_saved) == 0:
        stock_fund_industry_intraday_create = StockFundIndustryIntraday(trade_date=trade_date,
                                                                        name=name,
                                                                        index=index,
                                                                        change_rate=change_rate,
                                                                        change_rate_rank=change_rate_rank,
                                                                        fund_in=fund_in,
                                                                        fund_out=fund_out,
                                                                        net_amount=net_amount,
                                                                        firm_number=firm_number,
                                                                        best_stock=best_stock,
                                                                        best_change_rate=best_change_rate,
                                                                        best_latest_price=best_latest_price,
                                                                        created_at=created_at,
                                                                        updated_at=updated_at)
        db_stock_fund_industry_intraday = StockFundIndustryIntraday.model_validate(stock_fund_industry_intraday_create)
        session.add(db_stock_fund_industry_intraday)
        return 1
    else:
        return 0


def get_stock_fund_industry_intraday_items(session, name, trade_date):
    statement = (select(StockFundIndustryIntraday).where(StockFundIndustryIntraday.name == name).
                 where(StockFundIndustryIntraday.trade_date == trade_date))
    items = session.execute(statement).all()
    return items

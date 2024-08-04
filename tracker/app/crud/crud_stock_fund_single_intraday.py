# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     crud_stock_fund_single_intraday
   Description :
   Author :       EveryFine
   Date：          2024/7/25
-------------------------------------------------
   Change Activity:
                   2024/7/25:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

import datetime
from decimal import Decimal

import akshare as ak
from sqlmodel import Session, select

from app.common.log import log
from app.crud.crud_stock_trade_date import get_last_trade_date, get_last_trade_date_by_date
from app.models.stock_fund_single_intraday import StockFundSingleIntraday


def create_stock_fund_single_intraday(*, session: Session) -> int:
    total_count = 0
    trade_date = get_last_trade_date(session=session, final_datetime=datetime.datetime.now())
    stock_fund_single_intraday_ths_df = ak.stock_fund_flow_individual(symbol="即时")
    for index, row in stock_fund_single_intraday_ths_df.iterrows():
        res = create_stock_fund_single_intraday_item(session, trade_date, row)
        total_count += res
        if total_count > 0 and total_count % 100 == 0:
            session.commit()
    session.commit()
    log.info(f'creat stock fund single intraday(个股资金流--即时) finish, created count: {total_count}')
    return total_count


def per_str_to_float(per_str: str) -> float:
    res = float(per_str.strip('%'))
    return res


def fund_str_to_float(fund_str: str) -> float:
    """
    将包含中文单位的字符串转换为浮点数。
    :param fund_str:包含中文单位的字符串（如 "2.38亿", "3341.45万"）
    :return: 转换后的浮点数
    """
    if '亿' in fund_str:
        return float(Decimal(fund_str.replace('亿', '')) * Decimal(10000.0))
    elif '万' in fund_str:
        return float(Decimal(fund_str.replace('万', '')))
    else:
        return 0


def create_stock_fund_single_intraday_item(session, trade_date, row):
    symbol = f"{row['股票代码']:06d}"
    name = row['股票简称']
    latest_price = row['最新价']
    change_rate = per_str_to_float(row['涨跌幅'])
    change_rate_rank = row['序号']
    turnover_rate = per_str_to_float(row['换手率'])
    fund_in = fund_str_to_float(row['流入资金'])
    fund_out = fund_str_to_float(row['流出资金'])
    net_amount = fund_str_to_float(row['净额'])
    turnover = fund_str_to_float(row['成交额'])
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()

    items_saved = get_stock_fund_single_intraday_items(session, symbol, trade_date)
    if items_saved is None or len(items_saved) == 0:
        stock_fund_single_intraday_create = StockFundSingleIntraday(trade_date=trade_date, symbol=symbol, name=name,
                                                                    latest_price=latest_price, change_rate=change_rate,
                                                                    change_rate_rank=change_rate_rank,
                                                                    turnover_rate=turnover_rate,
                                                                    fund_in=fund_in, fund_out=fund_out,
                                                                    net_amount=net_amount,
                                                                    turnover=turnover, created_at=created_at,
                                                                    updated_at=updated_at)
        db_stock_fund_single_intraday = StockFundSingleIntraday.model_validate(stock_fund_single_intraday_create)
        session.add(db_stock_fund_single_intraday)
        return 1
    else:
        return 0


def get_stock_fund_single_intraday_items(session, symbol, trade_date):
    statement = (select(StockFundSingleIntraday).where(StockFundSingleIntraday.symbol == symbol).
                 where(StockFundSingleIntraday.trade_date == trade_date))
    items = session.execute(statement).all()
    return items


def check_stock_fund_single_intraday_date(session, check_date):
    last_trade_date = get_last_trade_date_by_date(session=session, final_date=check_date)
    statement = select(StockFundSingleIntraday).where(
        StockFundSingleIntraday.trade_date == last_trade_date)
    items = session.execute(statement).all()
    if items is None or len(items) == 0:
        return False
    else:
        return True



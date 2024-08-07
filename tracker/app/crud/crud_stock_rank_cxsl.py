# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     crud_stock_rank_cxsl
   Description :    技术指标 -- 持续缩量
   Author :       EveryFine
   Date：          2024/7/21
-------------------------------------------------
   Change Activity:
                   2024/7/21:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

import datetime
import re

import akshare as ak
from sqlmodel import Session, select

from app.common.log import log
from app.crud.crud_stock_trade_date import get_last_trade_date, get_last_trade_date_by_date
from app.models.stock_rank_cxsl import StockRankCxsl


def create_stock_rank_cxsl(*, session: Session) -> int:
    cxsl_count = 0
    trade_date = get_last_trade_date(session=session, final_datetime=datetime.datetime.now())
    stock_rank_cxsl_ths_df = ak.stock_rank_cxsl_ths()
    for index, row in stock_rank_cxsl_ths_df.iterrows():
        res = create_stock_rank_cxsl_item(session, trade_date, row)
        cxsl_count += res
        if cxsl_count > 0 and cxsl_count % 100 == 0:
            session.commit()
    session.commit()
    log.info(f'creat stock rank cxsl finish, created count: {cxsl_count}')
    return cxsl_count


def create_stock_rank_cxsl_item(session, trade_date, row):
    symbol = row['股票代码']
    name = row['股票简称']
    change_rate = row['涨跌幅']
    latest_price = row['最新价']
    base_date = getBaseDate(row['基准日成交量'])
    fl_days = row['缩量天数']
    days_change_rate = row['阶段涨跌幅']
    industry = row['所属行业']
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()

    items_saved = get_stock_rank_cxsl_items(session, symbol, trade_date)
    if items_saved is None or len(items_saved) == 0:
        stock_rank_cxsl_create = StockRankCxsl(trade_date=trade_date, symbol=symbol, name=name, change_rate=change_rate,
                                               latest_price=latest_price, base_date=base_date, fl_days=fl_days,
                                               days_change_rate=days_change_rate, industry=industry,
                                               created_at=created_at,
                                               updated_at=updated_at)
        db_stock_rank_cxsl = StockRankCxsl.model_validate(stock_rank_cxsl_create)
        session.add(db_stock_rank_cxsl)
        return 1
    else:
        return 0


def getBaseDate(base_date_desc):
    # 定义正则表达式模式来匹配日期部分
    pattern = r"\((\d{2})月(\d{2})日\)"
    # 使用 re.search() 来查找匹配的部分
    match = re.search(pattern, base_date_desc)
    if match:
        # 提取月份和日期
        month = match.group(1)
        day = match.group(2)
        year = datetime.datetime.now().year
        return datetime.date(year, int(month), int(day))
    else:
        return None


def get_stock_rank_cxsl_items(session, symbol, trade_date):
    statement = (select(StockRankCxsl).where(StockRankCxsl.symbol == symbol).
                 where(StockRankCxsl.trade_date == trade_date))
    items = session.execute(statement).all()
    return items

def check_stock_rank_cxsl_date(session, check_date):
    last_trade_date = get_last_trade_date_by_date(session=session, final_date=check_date)
    statement = select(StockRankCxsl).where(
        StockRankCxsl.trade_date == last_trade_date)
    items = session.execute(statement).all()
    if items is None or len(items) == 0:
        return False
    else:
        return True

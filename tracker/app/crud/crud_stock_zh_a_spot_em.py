# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     crud_stock_zh_a_spot_em
   Description :
   Author :       EveryFine
   Date：          2025/9/7
-------------------------------------------------
   Change Activity:
                   2025/9/7:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

import datetime

import akshare as ak
from sqlmodel import Session, select

from app.common.log import log
from app.crud.crud_stock_zh_a_spot_em_realtime import get_value_with_hyphen
from app.models.stock_zh_a_spot_em import StockZhASpotEm


def create_stock_zh_a_spot_em(*, session: Session) -> int:
    total_count = 0
    trade_date = datetime.date.today()
    collect_time = datetime.datetime.now().time()
    stock_zh_a_spot_em_ths_df = ak.stock_zh_a_spot_em()

    # 去除NaN
    filtered_df = stock_zh_a_spot_em_ths_df.dropna(subset=['最新价'])

    for index, row in filtered_df.iterrows():
        res = create_stock_zh_a_spot_em_item(session, trade_date, collect_time, row)
        total_count += res
        if total_count > 0 and total_count % 100 == 0:
            session.commit()
    session.commit()
    log.info(f'creat stock zh a spot em realtime(沪深京A股实时行情数据) finish, created count: {total_count}')
    return total_count


def create_stock_zh_a_spot_em_item(session, trade_date, collect_time, row):
    symbol = row['代码']
    name = row['名称']
    latest_price = get_value_with_hyphen(row['最新价'])
    change_rate = get_value_with_hyphen(row['涨跌幅'])

    change_amount = get_value_with_hyphen(row['涨跌额'])
    volume = get_value_with_hyphen(row['成交量'])

    turnover = get_value_with_hyphen(row['成交额'])
    range = get_value_with_hyphen(row['振幅'])

    high = get_value_with_hyphen(row['最高'])
    low = get_value_with_hyphen(row['最低'])

    open = get_value_with_hyphen(row['今开'])
    pre_close = get_value_with_hyphen(row['昨收'])

    volume_ratio = get_value_with_hyphen(row['量比'])
    turnover_rate = get_value_with_hyphen(row['换手率'])

    forward_pe_ratio = get_value_with_hyphen(row['市盈率-动态'])
    pb_mrq = get_value_with_hyphen(row['市净率'])
    market_value = get_value_with_hyphen(row['总市值'])
    traded_market_value = get_value_with_hyphen(row['流通市值'])
    up_speed = get_value_with_hyphen(row['涨速'])
    change_rate_5min = get_value_with_hyphen(row['5分钟涨跌'])
    change_rate_60d = get_value_with_hyphen(row['60日涨跌幅'])
    change_rate_ytd = get_value_with_hyphen(row['年初至今涨跌幅'])

    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()
    items_saved = get_stock_zh_a_spot_em_items(session, symbol, trade_date)
    if items_saved is None or len(items_saved) == 0:
        stock_zh_a_spot_em_create = StockZhASpotEm(trade_date=trade_date,
                                                   collect_time=collect_time,
                                                   symbol=symbol,
                                                   name=name,
                                                   latest_price=latest_price,
                                                   change_rate=change_rate,
                                                   change_amount=change_amount,
                                                   volume=volume,
                                                   turnover=turnover,
                                                   range=range,
                                                   high=high,
                                                   low=low,
                                                   open=open,
                                                   pre_close=pre_close,
                                                   volume_ratio=volume_ratio,
                                                   turnover_rate=turnover_rate,
                                                   forward_pe_ratio=forward_pe_ratio,
                                                   pb_mrq=pb_mrq,
                                                   market_value=market_value,
                                                   traded_market_value=traded_market_value,
                                                   up_speed=up_speed,
                                                   change_rate_5min=change_rate_5min,
                                                   change_rate_60d=change_rate_60d,
                                                   change_rate_ytd=change_rate_ytd,
                                                   created_at=created_at,
                                                   updated_at=updated_at)
        db_stock_zh_a_spot_em = StockZhASpotEm.model_validate(
            stock_zh_a_spot_em_create)
        session.add(db_stock_zh_a_spot_em)
        return 1
    else:
        return 0


def get_stock_zh_a_spot_em_items(session, symbol, trade_date):
    statement = (select(StockZhASpotEm).where(StockZhASpotEm.symbol == symbol).
                 where(StockZhASpotEm.trade_date == trade_date))
    items = session.execute(statement).all()
    return items

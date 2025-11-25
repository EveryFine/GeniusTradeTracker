# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     crud_stock_zh_a_spot_sina_realtime
   Description :
   Author :       EveryFine
   Date：          2025/11/25
-------------------------------------------------
   Change Activity:
                   2025/11/25:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

import datetime
import math

import akshare as ak
from sqlmodel import Session

from app.common.log import log
from app.models.stock_zh_a_spot_sina_realtime import StockZhASpotSinaRealtime


def create_stock_zh_a_spot_sina_realtime(*, session: Session) -> int:
    total_count = 0
    trade_date = datetime.date.today()
    collect_time = datetime.datetime.now()
    stock_zh_a_spot_sina_realtime_df = ak.stock_zh_a_spot()

    for index, row in stock_zh_a_spot_sina_realtime_df.iterrows():
        res = create_stock_zh_a_spot_sina_realtime_item(session, trade_date, collect_time, row)
        total_count += res
        if total_count > 0 and total_count % 100 == 0:
            session.commit()
    session.commit()
    log.info(f'creat stock zh a spot em realtime(沪深京A股实时行情数据) finish, created count: {total_count}')
    return total_count


def create_stock_zh_a_spot_sina_realtime_item(session, trade_date, collect_time, row):
    code = row['代码']
    symbol = code[2:]  # 去掉前缀sh/sz
    name = row['名称']
    latest_price = row['最新价']
    change_amount = row['涨跌额']
    change_rate = row['涨跌幅']
    buy_in = row['买入']
    sell_out = row['卖出']
    pre_close = row['昨收']
    open = row['今开']
    high = row['最高']
    low = row['最低']
    volume = row['成交量']

    turnover = row['成交额']
    data_timestamp = row['时间戳']

    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()

    stock_zh_a_spot_sina_realtime_create = StockZhASpotSinaRealtime(trade_date=trade_date,
                                                                    collect_time=collect_time,
                                                                    code=code,
                                                                    symbol=symbol,
                                                                    name=name,
                                                                    latest_price=latest_price,
                                                                    change_amount=change_amount,
                                                                    change_rate=change_rate,
                                                                    buy_in=buy_in,
                                                                    sell_out=sell_out,
                                                                    pre_close=pre_close,
                                                                    open=open,
                                                                    high=high,
                                                                    low=low,
                                                                    volume=volume,
                                                                    turnover=turnover,
                                                                    data_timestamp=data_timestamp,
                                                                    created_at=created_at,
                                                                    updated_at=updated_at)
    db_stock_zh_a_spot_sina_realtime = StockZhASpotSinaRealtime.model_validate(
        stock_zh_a_spot_sina_realtime_create)
    session.add(db_stock_zh_a_spot_sina_realtime)
    return 1


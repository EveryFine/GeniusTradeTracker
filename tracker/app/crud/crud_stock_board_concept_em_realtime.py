# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     crud_stock_board_concept_em_realtime
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

from sqlmodel import Session, select

from app.common.log import log
from app.crud.crud_stock_trade_date import get_last_trade_date
import akshare as ak

from app.models.stock_board_concept_em_realtime import StockBoardConceptEmRealtime


def create_stock_board_concept_em_realtime(*, session: Session) -> int:
    create_count = 0
    trade_date = get_last_trade_date(session=session, final_datetime=datetime.datetime.now())
    stock_board_concept_em_realtime_ths_df = ak.stock_board_concept_name_em()
    collect_time = datetime.datetime.now()
    for index, row in stock_board_concept_em_realtime_ths_df.iterrows():
        res = create_stock_board_concept_em_realtime_item(session, trade_date, collect_time, row)
        create_count += res
        if create_count > 0 and create_count % 100 == 0:
            session.commit()
    session.commit()
    log.info(f'creat stock board concept em finish, created count: {create_count}')
    return create_count


def create_stock_board_concept_em_realtime_item(session, trade_date, collect_time, row):
    rank = row['排名']
    name = row['板块名称']
    symbol = row['板块代码']
    latest_price = row['最新价']
    change_amount = row['涨跌额']
    change_rate = row['涨跌幅']
    market_value = row['总市值']
    turnover_rate = row['换手率']
    sz_count = row['上涨家数']
    xd_count = row['下跌家数']
    lz_symbol = row['领涨股票']
    lz_symbol_change_rate = row['领涨股票-涨跌幅']
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()

    stock_board_concept_em_realtime_create = StockBoardConceptEmRealtime(trade_date=trade_date,
                                                                         collect_time=collect_time,
                                                                         rank=rank,
                                                                         name=name,
                                                                         symbol=symbol,
                                                                         latest_price=latest_price,
                                                                         change_amount=change_amount,
                                                                         change_rate=change_rate,
                                                                         market_value=market_value,
                                                                         turnover_rate=turnover_rate,
                                                                         sz_count=sz_count,
                                                                         xd_count=xd_count,
                                                                         lz_symbol=lz_symbol,
                                                                         lz_symbol_change_rate=lz_symbol_change_rate,
                                                                         created_at=created_at,
                                                                         updated_at=updated_at)
    db_stock_board_concept_em_realtime = StockBoardConceptEmRealtime.model_validate(
        stock_board_concept_em_realtime_create)
    session.add(db_stock_board_concept_em_realtime)
    return 1

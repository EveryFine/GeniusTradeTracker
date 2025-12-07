# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     crud_stock_cyq_em
   Description :
   Author :       EveryFine
   Date：          2025/6/8
-------------------------------------------------
   Change Activity:
                   2025/6/8:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

import datetime
import time

from sqlmodel import Session, select
from fastapi import Query
from app.crud.crud_stock_info import get_all_stocks, get_stock_infos
import akshare as ak
from app.common.log import log
from app.models.stock_cyq_em import StockCyqEm, StockCyqEmCreate


def create_stock_cyq_em(*, session: Session) -> int:
    stock_infos = get_all_stocks(session=session)
    cyq_count = create_cyq_em_by_list(session, stock_infos)
    return cyq_count


def create_part_stock_cyq_em(*, session: Session,
                             stock_offset: int = 0,
                             stock_limit: int = Query(default=1000, le=1000)) -> int:
    stock_infos_public = get_stock_infos(session=session, offset=stock_offset, limit=stock_limit)
    stock_infos = stock_infos_public.data
    history_count = create_cyq_em_by_list(session, stock_infos)
    return history_count


def create_cyq_em_by_list(session, stock_infos):
    cyq_count = 0
    for stock_info in stock_infos:
        time.sleep(0.5)  # 避免请求过快被封IP
        stock_cyq_em_df = ak.stock_cyq_em(symbol=stock_info.symbol, adjust="")
        for index, row in stock_cyq_em_df.iterrows():
            res = create_stock_cyq_em_item(session=session, row=row, symbol=stock_info.symbol,
                                           name=stock_info.short_name)
            cyq_count += res
        session.commit()
    log.info(f'creat cyq em(筹码分布) by list finish, created count: {cyq_count}')
    return cyq_count


def create_stock_cyq_em_item(session, row, symbol, name):
    trade_date = row['日期']
    profit_ratio = row['获利比例']
    avg_cost = row['平均成本']
    cost_90_low = row['90成本-低']
    cost_90_high = row['90成本-高']
    concentration_90 = row['90集中度']
    cost_70_low = row['70成本-低']
    cost_70_high = row['70成本-高']
    concentration_70 = row['70集中度']
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()
    cyq_items_saved = get_stock_cyq_items(session, symbol, trade_date)
    if cyq_items_saved is None or len(cyq_items_saved) == 0:
        stock_cyq_em_create = StockCyqEmCreate(trade_date=trade_date,
                                               symbol=symbol,
                                               name=name,
                                               profit_ratio=profit_ratio,
                                               avg_cost=avg_cost,
                                               cost_90_low=cost_90_low,
                                               cost_90_high=cost_90_high,
                                               concentration_90=concentration_90,
                                               cost_70_low=cost_70_low,
                                               cost_70_high=cost_70_high,
                                               concentration_70=concentration_70,
                                               created_at=created_at, updated_at=updated_at)
        db_stock_cyq_em = StockCyqEm.model_validate(stock_cyq_em_create)
        session.add(db_stock_cyq_em)
        res = 1
        return res
    else:
        return 0


def get_stock_cyq_items(session, symbol, trade_date):
    statement = select(StockCyqEm).where(StockCyqEm.symbol == symbol).where(StockCyqEm.trade_date == trade_date)
    stock_cyq_items = session.execute(statement).all()
    return stock_cyq_items

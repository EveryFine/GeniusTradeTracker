# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     crud_stock_rank_xzjp
   Description :    技术指标 -- 险资举牌
   Author :       EveryFine
   Date：          2024/7/22
-------------------------------------------------
   Change Activity:
                   2024/7/22:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

import datetime

import akshare as ak
from sqlmodel import Session, select

from app.common.log import log
from app.crud.crud_stock_trade_date import get_last_trade_date
from app.models.stock_rank_xzjp import StockRankXzjp


def create_stock_rank_xzjp(*, session: Session) -> int:
    xzjp_count = 0
    stock_rank_xzjp_ths_df = ak.stock_rank_xzjp_ths()
    for index, row in stock_rank_xzjp_ths_df.iterrows():
        res = create_stock_rank_xzjp_item(session, row)
        xzjp_count += res
        if xzjp_count > 0 and xzjp_count % 100 == 0:
            session.commit()
    session.commit()
    log.info(f'creat stock rank xzjp finish, created count: {xzjp_count}')
    return xzjp_count


def create_stock_rank_xzjp_item(session, row):
    pub_date = row['举牌公告日']
    symbol = row['股票代码']
    name = row['股票简称']
    current_price = row['现价']
    change_rate = row['涨跌幅']
    pub_owner = row['举牌方']

    increase_amount = row['增持数量']
    increase_amount_per = row['增持数量占总股本比例']
    total_amount = row['变动后持股总数']
    total_amount_per = row['变动后持股比例']
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()

    items_saved = get_stock_rank_xzjp_items(session, symbol, pub_date, pub_owner)
    if items_saved is None or len(items_saved) == 0:
        stock_rank_xzjp_create = StockRankXzjp(pub_date=pub_date, symbol=symbol, name=name, current_price=current_price,
                                               change_rate=change_rate, pub_owner=pub_owner,
                                               increase_amount=increase_amount, increase_amount_per=increase_amount_per,
                                               total_amount=total_amount, total_amount_per=total_amount_per,
                                               created_at=created_at, updated_at=updated_at)
        db_stock_rank_xzjp = StockRankXzjp.model_validate(stock_rank_xzjp_create)
        session.add(db_stock_rank_xzjp)
        return 1
    else:
        return 0


def get_stock_rank_xzjp_items(session, symbol, pub_date, pub_owner):
    statement = (select(StockRankXzjp).where(StockRankXzjp.symbol == symbol).
                 where(StockRankXzjp.pub_date == pub_date).where(StockRankXzjp.pub_owner == pub_owner))
    items = session.execute(statement).all()
    return items


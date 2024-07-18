# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     crud_stock_comment
   Description :
   Author :       EveryFine
   Date：          2024/7/18
-------------------------------------------------
   Change Activity:
                   2024/7/18:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

from datetime import datetime

import akshare as ak
from sqlmodel import Session, select

from app.common.log import log
from app.models.stock_comment import StockComment


def create_stock_comments(*, session: Session) -> int:
    comment_count = 0
    stock_comment_em_df = ak.stock_comment_em()
    for index, row in stock_comment_em_df.iterrows():
        res = create_stock_comment_item(session=session, row=row)
        comment_count += res
        if comment_count % 100 == 0:
            session.commit()
    session.commit()
    log.info(f'creat stock comments finish, created count: {comment_count}')
    return comment_count


def create_stock_comment_item(session, row):
    symbol = row['代码']
    trade_date = row['交易日']
    name = row['名称']
    latest_price = row['最新价']
    change_rate = row['涨跌幅']

    turnover_rate = row['换手率']
    pe_ratio = row['市盈率']
    main_cost = row['主力成本']
    inst_own_pct = row['机构参与度']
    overall_score = row['综合得分']
    rise = row['上升']
    rank = row['目前排名']
    attention_index = row['关注指数']

    created_at = datetime.now()
    updated_at = datetime.now()

    comment_items_saved = get_stock_comment_items(session, symbol, trade_date)
    if comment_items_saved is None or len(comment_items_saved) == 0:
        stock_comment_create = StockComment(symbol=symbol, trade_date=trade_date, name=name, latest_price=latest_price,
                                            change_rate=change_rate, turnover_rate=turnover_rate, pe_ratio=pe_ratio,
                                            main_cost=main_cost, inst_own_pct=inst_own_pct, overall_score=overall_score,
                                            rise=rise, rank=rank, attention_index=attention_index,
                                            created_at=created_at, updated_at=updated_at)
        session.add(stock_comment_create)
        res = 1
        return res
    else:
        return 0


def get_stock_comment_items(session, symbol, trade_date):
    statement = select(StockComment).where(StockComment.symbol == symbol).where(
        StockComment.trade_date == trade_date)
    stock_comment_items = session.execute(statement).all()
    return stock_comment_items

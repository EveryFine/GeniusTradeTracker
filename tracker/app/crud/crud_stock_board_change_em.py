# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     crud_stock_board_change_em
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
import json

from sqlmodel import Session, select

from app.common.log import log
from app.crud.crud_stock_trade_date import get_last_trade_date
import akshare as ak

from app.models.stock_board_change_em import StockBoardChangeEm


def create_stock_board_change_em(*, session: Session) -> int:
    create_count = 0
    trade_date = get_last_trade_date(session=session, final_datetime=datetime.datetime.now())
    stock_board_change_em_df = ak.stock_board_change_em()
    collect_time = datetime.datetime.now()
    for index, row in stock_board_change_em_df.iterrows():
        res = create_stock_board_change_em_item(session, trade_date, collect_time, row)
        create_count += res
        if create_count > 0 and create_count % 100 == 0:
            session.commit()
    session.commit()
    log.info(f'creat stock board change em finish, created count: {create_count}')
    return create_count


def create_stock_board_change_em_item(session, trade_date, collect_time, row):

    name = row['板块名称']
    change_rate = row['涨跌幅']
    main_in = row['主力净流入']
    board_abnormal_count = int(row['板块异动总次数'])
    abnormal_most_stock_symbol = row['板块异动最频繁个股及所属类型-股票代码']
    abnormal_most_stock_name = row['板块异动最频繁个股及所属类型-股票名称']
    abnormal_most_action_type = row['板块异动最频繁个股及所属类型-买卖方向']
    abnormal_action_type_list = str(row['板块具体异动类型列表及出现次数'])
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()

    items_saved = get_stock_board_change_em_items(session, name, collect_time)
    if items_saved is None or len(items_saved) == 0:
        stock_board_change_em_create = StockBoardChangeEm(trade_date=trade_date,
                                                              collect_time=collect_time,
                                                              name=name,
                                                              change_rate=change_rate,
                                                              main_in=main_in,
                                                              board_abnormal_count=board_abnormal_count,
                                                              abnormal_most_stock_symbol=abnormal_most_stock_symbol,
                                                              abnormal_most_stock_name=abnormal_most_stock_name,
                                                              abnormal_most_action_type=abnormal_most_action_type,
                                                              abnormal_action_type_list=abnormal_action_type_list,
                                                              created_at=created_at,
                                                              updated_at=updated_at)
        db_stock_board_change_em = StockBoardChangeEm.model_validate(stock_board_change_em_create)
        session.add(db_stock_board_change_em)
        return 1
    else:
        return 0


def get_stock_board_change_em_items(session, name, collect_time):
    statement = (select(StockBoardChangeEm).where(StockBoardChangeEm.name == name).
                 where(StockBoardChangeEm.collect_time == collect_time))
    items = session.execute(statement).all()
    return items

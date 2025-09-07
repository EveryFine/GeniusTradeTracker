# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     crud_stock_board_industry_cons_em
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
import time

import akshare as ak
from sqlmodel import select, Session
from app.common.log import log

from app.models.stock_board_industry_cons_em import StockBoardIndustryConsEm


def create_stock_board_industry_cons_em(*, session: Session) -> int:
    create_count = 0
    stock_board_industry_em_df = ak.stock_board_industry_name_em()
    for index, row in stock_board_industry_em_df.iterrows():
        res = create_stock_board_industry_cons_em_item(session, row)
        create_count += res
        if create_count > 0 and create_count % 100 == 0:
            session.commit()
        time.sleep(1)
    session.commit()
    log.info(f'creat stock board industry em finish, created count: {create_count}')
    return create_count


def create_stock_board_industry_cons_em_item(session, board_row):
    board_name = board_row['板块名称']
    board_symbol = board_row['板块代码']

    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()
    stock_board_industry_cons_em_df = ak.stock_board_industry_cons_em(symbol=board_symbol)
    cons_count = 0
    for index, stock_row in stock_board_industry_cons_em_df.iterrows():
        stock_name = stock_row['名称']
        stock_symbol = stock_row['代码']
        items_saved = get_stock_board_industry_cons_em_items(session, board_symbol, stock_symbol)
        if items_saved is None or len(items_saved) == 0:
            stock_board_industry_cons_em_create = StockBoardIndustryConsEm(
                board_name=board_name,
                board_symbol=board_symbol,
                stock_name=stock_name,
                stock_symbol=stock_symbol,
                created_at=created_at,
                updated_at=updated_at)
            db_stock_board_industry_cons_em = StockBoardIndustryConsEm.model_validate(
                stock_board_industry_cons_em_create)
            session.add(db_stock_board_industry_cons_em)
            cons_count += 1
        else:
            cons_count += 0
    return cons_count


def get_stock_board_industry_cons_em_items(session, board_symbol, stock_symbol):
    statement = (select(StockBoardIndustryConsEm).where(StockBoardIndustryConsEm.board_symbol == board_symbol).
                 where(StockBoardIndustryConsEm.stock_symbol == stock_symbol))
    items = session.execute(statement).all()
    return items

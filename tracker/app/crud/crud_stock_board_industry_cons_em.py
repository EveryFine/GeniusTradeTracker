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
import random

from app.crud.crud_stock_board_industry_em import get_unique_board_symbols_last_year
from app.crud.crud_stock_trade_date import get_last_trade_date
from app.models.stock_board_industry_cons_em import StockBoardIndustryConsEm
from app.models.stock_board_industry_em import StockBoardIndustryEm


def create_stock_board_industry_cons_em(*, session: Session) -> int:
    create_count = 0
    board_items = get_unique_board_symbols_last_year(session) or []
    board_items = list(board_items)
    random.shuffle(board_items)
    trade_date = get_last_trade_date(session=session, final_datetime=datetime.datetime.now())
    collect_time = datetime.datetime.now()
    for board_item in board_items:
        board_symbol = board_item['symbol']
        board_name = board_item['name']
        res = create_stock_board_industry_cons_em_item(session, board_symbol, board_name, trade_date, collect_time)
        create_count += res

        session.commit()
        time.sleep(1)
    session.commit()
    log.info(f'creat stock board industry em finish, created count: {create_count}')
    return create_count


def create_stock_board_industry_cons_em_item(session, board_symbol, board_name, trade_date, collect_time):

    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()
    stock_board_industry_cons_em_df = ak.stock_board_industry_cons_em(symbol=board_symbol)
    cons_count = 0
    for index, stock_row in stock_board_industry_cons_em_df.iterrows():
        stock_name = stock_row.get('名称')
        stock_symbol = stock_row.get('代码')
        stock_index = stock_row.get('序号')
        latest_price = stock_row.get('最新价')
        change_rate = stock_row.get('涨跌幅')
        change_amount = stock_row.get('涨跌额')
        volume = stock_row.get('成交量')
        turnover = stock_row.get('成交额')
        range_ = stock_row.get('振幅')
        high = stock_row.get('最高')
        low = stock_row.get('最低')
        open_ = stock_row.get('今开')
        pre_close = stock_row.get('昨收')
        turnover_rate = stock_row.get('换手率')
        forward_pe_ratio = stock_row.get('市盈率-动态')
        pb_mrq = stock_row.get('市净率')
        items_saved = get_stock_board_industry_cons_em_items(session, board_symbol, stock_symbol, collect_time)
        if items_saved is None or len(items_saved) == 0:
            stock_board_industry_cons_em_create = StockBoardIndustryConsEm(
                trade_date=trade_date,
                collect_time=collect_time,
                board_name=board_name,
                board_symbol=board_symbol,
                stock_name=stock_name,
                stock_symbol=stock_symbol,
                stock_index=stock_index,
                latest_price=latest_price,
                change_rate=change_rate,
                change_amount=change_amount,
                volume=volume,
                turnover=turnover,
                range=range_,
                high=high,
                low=low,
                open=open_,
                pre_close=pre_close,
                turnover_rate=turnover_rate,
                forward_pe_ratio=forward_pe_ratio,
                pb_mrq=pb_mrq,
                created_at=created_at,
                updated_at=updated_at)
            db_stock_board_industry_cons_em = StockBoardIndustryConsEm.model_validate(
                stock_board_industry_cons_em_create)
            session.add(db_stock_board_industry_cons_em)
            cons_count += 1
        else:
            cons_count += 0
    return cons_count


def get_stock_board_industry_cons_em_items(session, board_symbol, stock_symbol, collect_time):
    statement = (select(StockBoardIndustryConsEm).where(StockBoardIndustryConsEm.board_symbol == board_symbol).
                 where(StockBoardIndustryConsEm.stock_symbol == stock_symbol).where(StockBoardIndustryConsEm.collect_time == collect_time))
    items = session.exec(statement).all()
    return items


def create_stock_board_industry_cons_em_by_board_name(*, session: Session, board_name) -> int:
    """Create industry constituents by board name (or board code)."""
    # try to find symbol by name
    statement = select(StockBoardIndustryEm).where(StockBoardIndustryEm.name == board_name)
    items = session.exec(statement).all()
    board_symbol = None
    if items and len(items) > 0:
        board_symbol = items[0].symbol
    else:
        # maybe user passed the symbol directly
        board_symbol = board_name

    trade_date = get_last_trade_date(session=session, final_datetime=datetime.datetime.now())
    collect_time = datetime.datetime.now()
    res = create_stock_board_industry_cons_em_item(session, board_symbol, board_name, trade_date, collect_time)
    session.commit()
    log.info(f'create stock board industry cons em(board_symbol:{board_symbol},board_name:{board_name}) finish, created count: {res}')
    return res



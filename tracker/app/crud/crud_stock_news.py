# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     crud_stock_news
   Description :
   Author :       EveryFine
   Date：          2024/7/15
-------------------------------------------------
   Change Activity:
                   2024/7/15:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

import datetime

from fastapi import Query
from sqlmodel import Session, select
import akshare as ak

from app.common.log import log
from app.crud.crud_stock_info import get_all_stocks, get_stock_infos
from app.crud.crud_stock_trade_date import get_last_trade_date, get_last_trade_date_by_date
from app.models.stock_news import StockNews, StockNewsCreate


def create_stock_news(*, session: Session) -> int:
    stock_infos = get_all_stocks(session=session)
    news_count = create_news_by_list(session, stock_infos)
    return news_count


def create_part_stock_news(*, session: Session, stock_offset: int = 0,
                           stock_limit: int = Query(default=1000, le=1000)) -> int:
    stock_infos_public = get_stock_infos(session=session, offset=stock_offset, limit=stock_limit)
    stock_infos = stock_infos_public.data
    history_count = create_news_by_list(session, stock_infos)
    return history_count


def create_news_by_list(session, stock_infos):
    news_count = 0
    for stock_info in stock_infos:
        stock_news_em_df = ak.stock_news_em(symbol=stock_info.symbol)
        for index, row in stock_news_em_df.iterrows():
            res = create_stock_news_item(session=session, row=row)
            news_count += res
        session.commit()
    log.info(f'creat news by list finish, created count: {news_count}')
    return news_count


def create_stock_news_item(session, row):
    symbol = row['关键词']
    pub_time = row['发布时间']
    title = row['新闻标题']
    content = row['新闻内容']
    source = row['文章来源']
    link = row['新闻链接']
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()
    news_items_saved = get_stock_news_items(session, symbol, pub_time)
    if news_items_saved is None or len(news_items_saved) == 0:
        stock_news_create = StockNewsCreate(symbol=symbol, pub_time=pub_time, title=title, content=content,
                                            source=source, link=link, created_at=created_at, updated_at=updated_at)
        db_stock_news = StockNews.model_validate(stock_news_create)
        session.add(db_stock_news)
        res = 1
        return res
    else:
        return 0


def get_stock_news_items(session, symbol, pub_time):
    statement = select(StockNews).where(StockNews.symbol == symbol).where(StockNews.pub_time == pub_time)
    stock_news_items = session.execute(statement).all()
    return stock_news_items


def check_stock_news_date(session, check_date):
    last_trade_date = get_last_trade_date_by_date(session=session, final_date=check_date)
    statement = select(StockNews).where(
        StockNews.pub_time.date() == last_trade_date)
    items = session.execute(statement).all()
    if items is None or len(items) == 0:
        return False
    else:
        return True



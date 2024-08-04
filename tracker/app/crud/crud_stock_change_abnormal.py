# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     crud_stock_change_abnormal
   Description :   盘口异动
   Author :       EveryFine
   Date：          2024/7/16
-------------------------------------------------
   Change Activity:
                   2024/7/16:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

import datetime

import akshare as ak
from sqlmodel import Session, select

from app.common.log import log
from app.crud.crud_stock_trade_date import get_last_trade_date, get_last_trade_date_by_date
from app.models.stock_change_abnormal import StockChangeAbnormal, StockChangeAbnormalCreate


def create_stock_change_abnormal(*, session: Session) -> int:
    abnormal_events = (
        '火箭发射', '快速反弹', '大笔买入', '封涨停板', '打开跌停板', '有大买盘', '竞价上涨', '高开5日线', '向上缺口',
        '60日新高', '60日大幅上涨', '加速下跌', '高台跳水', '大笔卖出', '封跌停板', '打开涨停板', '有大卖盘',
        '竞价下跌',
        '低开5日线', '向下缺口', '60日新低', '60日大幅下跌')
    events_count = create_change_abnormal_by_events(session, abnormal_events)
    return events_count


def create_change_abnormal_by_events(session, abnormal_events):
    change_count = 0
    for event in abnormal_events:
        res = create_stock_change_abnormal_by_event(session, event)
        change_count += res
    return change_count


def create_stock_change_abnormal_by_event(session, event):
    change_event_count = 0
    stock_changes_em_df = ak.stock_changes_em(symbol=event)
    for index, row in stock_changes_em_df.iterrows():
        res = create_stock_change_abnormal_item(session=session, row=row)
        change_event_count += res
    session.commit()
    log.info(f'creat stock change abnormal by event finish, event:{event}, created count: {change_event_count}')
    return change_event_count


def create_stock_change_abnormal_item(session, row):
    last_trade_date = get_last_trade_date(session=session, final_datetime=datetime.datetime.now())
    symbol = row['代码']
    event_time = row['时间']
    name = row['名称']
    event = row['板块']
    attach_info = row['相关信息']
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()
    change_items_saved = get_stock_change_abnormal_items(session, symbol, last_trade_date, event_time, event)
    if change_items_saved is None or len(change_items_saved) == 0:
        stock_change_abnormal_create = StockChangeAbnormalCreate(symbol=symbol, date=last_trade_date,
                                                                 event_time=event_time, name=name, event=event,
                                                                 attach_info=attach_info, created_at=created_at,
                                                                 updated_at=updated_at)
        db_stock_change_abnormal = StockChangeAbnormal.model_validate(stock_change_abnormal_create)
        session.add(db_stock_change_abnormal)
        res = 1
        return res
    else:
        return 0


def get_stock_change_abnormal_items(session, symbol, last_trade_date, event_time, event):
    statement = select(StockChangeAbnormal).where(StockChangeAbnormal.symbol == symbol).where(
        StockChangeAbnormal.date == last_trade_date).where(StockChangeAbnormal.event_time == event_time).where(
        StockChangeAbnormal.event == event)
    stock_change_abnormal_items = session.execute(statement).all()
    return stock_change_abnormal_items


def check_stock_change_abnormal_date(session, check_date):
    last_trade_date = get_last_trade_date_by_date(session=session, final_date=check_date)

    abnormal_events = (
        '火箭发射', '快速反弹', '大笔买入', '封涨停板', '打开跌停板', '有大买盘', '竞价上涨', '高开5日线', '向上缺口',
        '60日新高', '60日大幅上涨', '加速下跌', '高台跳水', '大笔卖出', '封跌停板', '打开涨停板', '有大卖盘',
        '竞价下跌',
        '低开5日线', '向下缺口', '60日新低', '60日大幅下跌')
    for event in abnormal_events:
        statement = select(StockChangeAbnormal).where(StockChangeAbnormal.event == event).where(
            StockChangeAbnormal.date == last_trade_date)
        stock_change_abnormal_items = session.execute(statement).all()
        if stock_change_abnormal_items is None or len(stock_change_abnormal_items) == 0:
            return False
    return True

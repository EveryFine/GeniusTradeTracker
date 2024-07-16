# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     crud_stock_change_abnormal
   Description :
   Author :       EveryFine
   Date：          2024/7/16
-------------------------------------------------
   Change Activity:
                   2024/7/16:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

import akshare as ak
from sqlmodel import Session


def create_stock_change_abnormal(*, session: Session) -> int:
    abnormal_events = (
        '火箭发射', '快速反弹', '大笔买入', '封涨停板', '打开跌停板', '有大买盘', '竞价上涨', '高开5日线', '向上缺口',
        '60日新高', '60日大幅上涨', '加速下跌', '高台跳水', '大笔卖出', '封跌停板', '打开涨停板', '有大卖盘',
        '竞价下跌',
        '低开5日线', '向下缺口', '60日新低', '60日大幅下跌')
    events_count = create_change_abnormal_by_events(session, abnormal_events)
    return events_count


def create_change_abnormal_by_events(session, abnormal_events):
    for event in abnormal_events:
        create_stock_change_abnormal_by_event(session, event)



def create_stock_change_abnormal_by_event(session, event):
    stock_changes_em_df = ak.stock_changes_em(symbol=event)
    for index, row in stock_changes_em_df.iterrows():
        res = create_stock_change_abnormal_item(session=session, row=row)

def create_stock_change_abnormal_item(session, row):
    pass

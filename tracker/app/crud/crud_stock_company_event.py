# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     crud_stock_company_event
   Description :
   Author :       EveryFine
   Date：          2024/7/21
-------------------------------------------------
   Change Activity:
                   2024/7/21:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

from datetime import datetime, timedelta, date

from sqlmodel import Session, select
import akshare as ak

from app.common.log import log
from app.models.stock_company_event import StockCompanyEvent


def create_all_stock_company_events(*, session: Session) -> int:
    # 遍历2013年5月1日开始的日期，直到今天，2013.5.1之前无法查询到数据
    start_date = date(2013, 1, 1)
    # 获取今天的日期
    end_date = date.today()
    res = create_part_stock_company_events(session=session, start_date=start_date, end_date=end_date)
    return res


def create_part_stock_company_events(*, session: Session, start_date: date = date(2013, 1, 1),
                                     end_date=date.today()) -> int:
    events_count = 0
    # 当前遍历的日期
    current_date = start_date
    # 遍历从起始日期到截止日期的每一天
    while current_date <= end_date:
        date_count = 0
        formatted_date = current_date.strftime('%Y%m%d')
        try:
            stock_gsrl_gsdt_em_df = ak.stock_gsrl_gsdt_em(date=formatted_date)
        except Exception as e:
            log.info(f'creat stock company events date:{formatted_date}, error: {str(e)}')
        else:
            for index, row in stock_gsrl_gsdt_em_df.iterrows():
                res = create_stock_company_event_item(session=session, row=row)
                date_count += res
                events_count += res
                if events_count > 0 and events_count % 100 == 0:
                    session.commit()
            log.info(f'creat stock company events date:{formatted_date}, created count: {date_count}')
        finally:
            current_date += timedelta(days=1)
    session.commit()
    log.info(f'creat stock company events finish, created count: {events_count}')
    return events_count


def create_stock_company_event_item(session, row):
    symbol = row['代码']
    event_date = row['交易日']
    date_index = row['序号']
    name = row['简称']
    event_type = row['事件类型']
    event = row['具体事项'].replace('\x00', '')
    created_at = datetime.now()
    updated_at = datetime.now()

    event_items_saved = get_company_event_items(session, symbol, event_date, date_index)
    if event_items_saved is None or len(event_items_saved) == 0:
        event_create = StockCompanyEvent(symbol=symbol, name=name, event_type=event_type, event_date=event_date,
                                         date_index=date_index, event=event, created_at=created_at,
                                         updated_at=updated_at)
        db_event = StockCompanyEvent.model_validate(event_create)
        session.add(db_event)
        return 1
    else:
        return 0


def get_company_event_items(session, symbol, event_date, date_index):
    statement = select(StockCompanyEvent).where(StockCompanyEvent.symbol == symbol).where(
        StockCompanyEvent.event_date == event_date).where(StockCompanyEvent.date_index == date_index)
    items = session.execute(statement).all()
    return items

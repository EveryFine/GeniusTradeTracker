# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     crud_stock_pool_zt
   Description :  股池--涨停
   Author :       EveryFine
   Date：          2024/7/28
-------------------------------------------------
   Change Activity:
                   2024/7/28:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

from datetime import datetime, timedelta, date

from sqlmodel import Session, select
import akshare as ak

from app.common.log import log
from app.crud.crud_stock_trade_date import get_last_trade_date, get_last_trade_date_by_date
from app.models.stock_pool_zt import StockPoolZt


def create_stock_pool_zt(*, session: Session) -> int:
    # 接口最多可以查询两周之内的数据，此处遍历一周之内的数据
    start_date = date.today() - timedelta(days=7)
    # 获取今天的日期
    end_date = date.today()
    res = create_part_stock_pool_zt(session=session, start_date=start_date, end_date=end_date)
    return res


def create_part_stock_pool_zt(*, session: Session, start_date: date = date.today() - timedelta(days=7),
                              end_date=date.today()) -> int:
    zt_count = 0
    # 当前遍历的日期
    current_date = start_date
    # 遍历从起始日期到截止日期的每一天
    while current_date <= end_date:
        date_count = 0
        trade_date = get_last_trade_date_by_date(session=session, final_date=current_date)
        formatted_date = trade_date.strftime('%Y%m%d')
        try:
            stock_zt_pool_em_df = ak.stock_zt_pool_em(date=formatted_date)
        except Exception as e:
            log.info(f'creat stock pool zt date:{formatted_date}, error: {str(e)}')
        else:
            for index, row in stock_zt_pool_em_df.iterrows():
                res = create_stock_pool_zt_item(session=session, row=row, trade_date=trade_date)
                date_count += res
                zt_count += res
                if zt_count > 0 and zt_count % 100 == 0:
                    session.commit()
            log.info(f'creat stock pool zt(股池--涨停) date:{formatted_date}, created count: {date_count}')
        finally:
            current_date += timedelta(days=1)
    session.commit()
    log.info(f'creat stock pool zt(股池--涨停) finish, created count: {zt_count}')
    return zt_count


def get_time_from_str(time_str):
    res = datetime.strptime(time_str, '%H%M%S').time()
    return res


def create_stock_pool_zt_item(session, row, trade_date):
    symbol = row['代码']
    name = row['名称']
    change_rate = row['涨跌幅']
    latest_price = row['最新价']
    turnover = row['成交额']
    traded_market_value = row['流通市值']
    market_value = row['总市值']
    turnover_rate = row['换手率']
    fb_fund = row['封板资金']
    fb_first_time = get_time_from_str(row['首次封板时间'])
    fb_last_time = get_time_from_str(row['最后封板时间'])
    zb_count = row['炸板次数']
    zt_status = row['涨停统计']
    lb_count = row['连板数']
    industry = row['所属行业']

    created_at = datetime.now()
    updated_at = datetime.now()

    event_items_saved = get_pool_zt_items(session, symbol, trade_date)
    if event_items_saved is None or len(event_items_saved) == 0:
        event_create = StockPoolZt(trade_date=trade_date,
                                   symbol=symbol,
                                   name=name,
                                   change_rate=change_rate,

                                   latest_price=latest_price,
                                   turnover=turnover,
                                   traded_market_value=traded_market_value,
                                   market_value=market_value,
                                   turnover_rate=turnover_rate,
                                   fb_fund=fb_fund,
                                   fb_first_time=fb_first_time,
                                   fb_last_time=fb_last_time,
                                   zb_count=zb_count,
                                   zt_status=zt_status,
                                   lb_count=lb_count,
                                   industry=industry,
                                   created_at=created_at,
                                   updated_at=updated_at)
        db_event = StockPoolZt.model_validate(event_create)
        session.add(db_event)
        return 1
    else:
        return 0


def get_pool_zt_items(session, symbol, trade_date):
    statement = select(StockPoolZt).where(StockPoolZt.symbol == symbol).where(
        StockPoolZt.trade_date == trade_date)
    items = session.execute(statement).all()
    return items

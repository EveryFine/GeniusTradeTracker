# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     crud_stock_pool_strong
   Description :   股池--强势
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
from app.models.stock_pool_strong import StockPoolStrong


def create_stock_pool_strong(*, session: Session) -> int:
    # 接口最多可以查询两周之内的数据，此处遍历一周之内的数据
    start_date = date.today() - timedelta(days=7)
    # 获取今天的日期
    end_date = date.today()
    res = create_part_stock_pool_strong(session=session, start_date=start_date, end_date=end_date)
    return res


def create_part_stock_pool_strong(*, session: Session, start_date: date = date.today() - timedelta(days=7),
                                  end_date=date.today()) -> int:
    strong_count = 0
    # 当前遍历的日期
    current_date = start_date
    # 遍历从起始日期到截止日期的每一天
    while current_date <= end_date:
        date_count = 0
        trade_date = get_last_trade_date_by_date(session=session, final_date=current_date)
        formatted_date = trade_date.strftime('%Y%m%d')
        try:
            stock_zt_pool_strong_em_df = ak.stock_zt_pool_strong_em(date=formatted_date)
        except Exception as e:
            log.info(f'creat stock pool zt date:{formatted_date}, error: {str(e)}')
        else:
            for index, row in stock_zt_pool_strong_em_df.iterrows():
                res = create_stock_pool_strong_item(session=session, row=row, trade_date=trade_date)
                date_count += res
                strong_count += res
                if strong_count > 0 and strong_count % 100 == 0:
                    session.commit()
            log.info(
                f'creat stock pool strong(股池--强势) current_date: {current_date} ,trade_date:{formatted_date}, created count: {date_count}')
        finally:
            current_date += timedelta(days=1)
    session.commit()
    log.info(f'creat stock pool strong(股池--强势) finish, created count: {strong_count}')
    return strong_count


def get_time_from_str(time_str):
    res = datetime.strptime(time_str, '%H%M%S').time()
    return res


def create_stock_pool_strong_item(session, row, trade_date):
    symbol = row['代码']
    name = row['名称']
    change_rate = row['涨跌幅']
    latest_price = row['最新价']
    zt_price = row['涨停价']
    turnover = row['成交额']
    traded_market_value = row['流通市值']
    market_value = row['总市值']
    turnover_rate = row['换手率']
    up_speed = row['涨速']
    is_new_high = row['是否新高']
    volume_ratio = row['量比']
    zt_status = row['涨停统计']
    reason = row['入选理由']
    industry = row['所属行业']

    created_at = datetime.now()
    updated_at = datetime.now()

    event_items_saved = get_pool_strong_items(session, symbol, trade_date)
    if event_items_saved is None or len(event_items_saved) == 0:
        event_create = StockPoolStrong(trade_date=trade_date,
                                       symbol=symbol,
                                       name=name,
                                       change_rate=change_rate,
                                       latest_price=latest_price,
                                       zt_price=zt_price,
                                       turnover=turnover,
                                       traded_market_value=traded_market_value,
                                       market_value=market_value,
                                       turnover_rate=turnover_rate,
                                       up_speed=up_speed,
                                       is_new_high=is_new_high,
                                       volume_ratio=volume_ratio,

                                       zt_status=zt_status,
                                       reason=reason,
                                       industry=industry,
                                       created_at=created_at,
                                       updated_at=updated_at)
        db_event = StockPoolStrong.model_validate(event_create)
        session.add(db_event)
        return 1
    else:
        return 0


def get_pool_strong_items(session, symbol, trade_date):
    statement = select(StockPoolStrong).where(StockPoolStrong.symbol == symbol).where(
        StockPoolStrong.trade_date == trade_date)
    items = session.execute(statement).all()
    return items


def check_stock_pool_strong_date(session, check_date):
    last_trade_date = get_last_trade_date_by_date(session=session, final_date=check_date)
    statement = select(StockPoolStrong).where(
        StockPoolStrong.trade_date == last_trade_date)
    items = session.execute(statement).all()
    if items is None or len(items) == 0:
        return False
    else:
        return True

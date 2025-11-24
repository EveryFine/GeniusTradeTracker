# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     crud_stock_market_activity_realtime
   Description :
   Author :       EveryFine
   Date：          2025/11/24
-------------------------------------------------
   Change Activity:
                   2025/11/24:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

import datetime

import akshare as ak
import pandas as pd
from sqlmodel import Session

from app.common.log import log
from app.models.stock_market_activity_realtime import StockMarketActivityRealtime


def create_stock_market_activity_realtime(*, session: Session) -> int:
    total_count = 0
    trade_date = datetime.date.today()
    collect_time = datetime.datetime.now()
    stock_market_activity_realtime_df = ak.stock_market_activity_legu()

    res = create_stock_market_activity_realtime_item(session, trade_date, collect_time,
                                                     stock_market_activity_realtime_df)
    total_count += res

    session.commit()
    log.info(f'creat stock market activity realtime(赚钱效应分析) finish, created count: {total_count}')
    return total_count


def create_stock_market_activity_realtime_item(session, trade_date, collect_time, df):
    data = df.set_index('item')['value']
    advancing = data['上涨']
    limit_up = data['涨停']
    true_limit_up = data['真实涨停']
    st_limit_up = data['st st*涨停']
    declining = data['下跌']
    limit_down = data['跌停']
    true_limit_down = data['真实跌停']
    st_limit_down = data['st st*跌停']
    unchanged = data['平盘']
    suspended = data['停牌']
    activity_rate = float(data['活跃度'].rstrip('%'))
    statistical_date = pd.to_datetime(data['统计日期']).to_pydatetime()

    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()

    stock_market_activity_realtime_create = StockMarketActivityRealtime(trade_date=trade_date,
                                                                        collect_time=collect_time,
                                                                        advancing=advancing,
                                                                        limit_up=limit_up,
                                                                        true_limit_up=true_limit_up,
                                                                        st_limit_up=st_limit_up,
                                                                        declining=declining,
                                                                        limit_down=limit_down,
                                                                        true_limit_down=true_limit_down,
                                                                        st_limit_down=st_limit_down,
                                                                        unchanged=unchanged,
                                                                        suspended=suspended,
                                                                        activity_rate=activity_rate,
                                                                        statistical_date=statistical_date,
                                                                        created_at=created_at,
                                                                        updated_at=updated_at)
    db_stock_market_activity_realtime = StockMarketActivityRealtime.model_validate(
        stock_market_activity_realtime_create)
    session.add(db_stock_market_activity_realtime)
    return 1


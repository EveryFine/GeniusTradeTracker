# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     crud_stock_history_bao_k.py
   Description :
   Author :       EveryFine
   Date：          2025/5/2
-------------------------------------------------
   Change Activity:
                   2025/5/2:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

import datetime
import time
import traceback

import baostock as bs
from fastapi import Query
from sqlmodel import Session, select

from app.common.log import log
from app.crud.crud_stock_info import get_all_stocks, get_stock_infos
from app.crud.crud_stock_trade_date import get_last_trade_date_by_date
from app.models.stock_history_bao_k import StockHistoryBaoKCreate, StockHistoryBaoK


def create_stock_history_bao_k(*, session: Session) -> int:
    stock_infos = get_all_stocks(session=session)
    history_count = create_histories_by_list(session, stock_infos)
    return history_count


def create_histories_by_list(session, stock_infos):
    history_count = 0

    for stock_info in stock_infos:
        lg = bs.login()
        start_time_stock = time.time()  # 开始计时
        symbol = stock_info.symbol
        exchange = stock_info.exchange
        name = stock_info.short_name
        # start_time = time.time()  # 开始计时
        start_date = get_start_date(session=session, symbol=stock_info.symbol)

        end_date = '2050-01-01'
        ## baostock获取数据
        code = exchange + '.' + symbol
        # log.info(f"Get start date for {code} in {time.time() - start_time:.2f} seconds")
        # log.info(f"Fetching data for {code} from {start_date} to {end_date}")
        # start_time = time.time()  # 开始计时
        try:
            rs = bs.query_history_k_data_plus(code,
                                              "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,peTTM,psTTM,pcfNcfTTM,pbMRQ,isST",
                                              start_date=start_date, end_date=end_date,
                                              frequency="d", adjustflag="3")
            stock_bao_k_data = rs.get_data()
            # log.info(f"Data fetched for {code}, rows: {len(stock_bao_k_data)} in {time.time() - start_time:.2f} seconds")
            # start_time = time.time()  # 重置计时
            for index, row in stock_bao_k_data.iterrows():
                stock_hist = create_stock_hist_bao_k(session=session, row=row, symbol=symbol, name=name)
                history_count += 1
            session.commit()
            # log.info(f"Inserted {history_count} records for {code} in {time.time() - start_time:.2f} seconds")
            log.info(f"history bao k processing data for {code} from {start_date} to {end_date}, total in {time.time() - start_time_stock:.2f} seconds")
            bs.logout()
        except Exception as e:
            error_msg = f"{datetime.datetime.now()} history bao k processing data for {code} from {start_date} to {end_date} error: {str(e)}\n{traceback.format_exc()}"
            log.error(error_msg)
            bs.logout()

    return history_count


def create_part_stock_bao_k(*, session: Session, stock_offset: int = 0,
                            stock_limit: int = Query(default=1000, le=1000)) -> int:
    stock_infos_public = get_stock_infos(session=session, offset=stock_offset, limit=stock_limit)
    stock_infos = stock_infos_public.data
    history_count = create_histories_by_list(session, stock_infos)

    return history_count


def get_start_date(session, symbol) -> str:
    stock_hist = get_latest_stock_history(session, symbol)
    if stock_hist is None:
        return '1970-01-01'
    last_date = stock_hist.date
    query_start_date = last_date + datetime.timedelta(days=1)
    start_date_str = query_start_date.strftime("%Y-%m-%d")
    return start_date_str


def get_latest_stock_history(session, symbol):
    # 只获取最新的一条记录
    statement = (
        select(StockHistoryBaoK)
        .where(StockHistoryBaoK.symbol == symbol)
        .order_by(StockHistoryBaoK.date.desc())
        .limit(1)  # 限制只返回一条记录
    )
    result = session.execute(statement).first()
    return result[0] if result else None


def create_stock_hist_bao_k(session, row, symbol, name):
    code = row['code']
    date = row['date']
    open = empty_str_to_none(row['open'])
    close = empty_str_to_none(row['close'])
    high = empty_str_to_none(row['high'])
    low = empty_str_to_none(row['low'])
    volume = empty_str_to_none(row['volume'])
    pre_close = empty_str_to_none(row['preclose'])
    amount = empty_str_to_none(row['amount'])
    adjust_flag = empty_str_to_none(row['adjustflag'])
    turn = empty_str_to_none(row['turn'])
    trade_status = empty_str_to_none(row['tradestatus'])
    change_rate = empty_str_to_none(row['pctChg'])
    pe_ttm = empty_str_to_none(row['peTTM'])
    pb_mrq = empty_str_to_none(row['pbMRQ'])
    ps_ttm = empty_str_to_none(row['psTTM'])
    pcf_ncf_ttm = empty_str_to_none(row['pcfNcfTTM'])
    is_st = row['isST']
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()
    stock_hist_bao_k_create = StockHistoryBaoKCreate(code=code,
                                                     symbol=symbol,
                                                     name=name,
                                                     date=date,
                                                     open=open,
                                                     close=close,
                                                     high=high,
                                                     low=low,
                                                     volume=volume,
                                                     pre_close=pre_close,
                                                     amount=amount,
                                                     adjust_flag=adjust_flag,
                                                     turn=turn,
                                                     trade_status=trade_status,
                                                     change_rate=change_rate,
                                                     pe_ttm=pe_ttm,
                                                     pb_mrq=pb_mrq,
                                                     ps_ttm=ps_ttm,
                                                     pcf_ncf_ttm=pcf_ncf_ttm,
                                                     is_st=is_st,
                                                     created_at=created_at,
                                                     updated_at=updated_at
                                                     )
    # log.info(stock_hist_bao_k_create)
    db_stock_hist = StockHistoryBaoK.model_validate(stock_hist_bao_k_create)
    session.add(db_stock_hist)
    # session.commit()
    # session.refresh(db_stock_hist)
    res = StockHistoryBaoK.model_validate(db_stock_hist)
    return res


def empty_str_to_none(v):
    """将空值转换为none"""
    if v == '' or v is None:
        return None
    return v


def check_stock_history_date(session, check_date):
    last_trade_date = get_last_trade_date_by_date(session=session, final_date=check_date)
    statement = select(StockHistoryBaoK).where(
        StockHistoryBaoK.date == last_trade_date)
    items = session.execute(statement).all()
    if items is None or len(items) < 4000:
        return False
    else:
        return True

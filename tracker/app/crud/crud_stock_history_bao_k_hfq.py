# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     crud_stock_history_bao_k_hfq
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

import baostock as bs
from fastapi import Query
from sqlmodel import Session, select

from app.common.log import log
from app.crud.crud_stock_info import get_all_stocks, get_stock_infos
from app.crud.crud_stock_trade_date import get_last_trade_date_by_date
from app.models.stock_history_bao_k_hfq import StockHistoryBaoKHfqCreate, StockHistoryBaoKHfq


def create_stock_history_bao_k_hfq(*, session: Session) -> int:
    stock_infos = get_all_stocks(session=session)
    history_count = create_histories_by_list(session, stock_infos)
    return history_count


def create_histories_by_list(session, stock_infos):
    history_count = 0
    for stock_info in stock_infos:
        symbol = stock_info.symbol
        exchange = stock_info.exchange
        name = stock_info.short_name
        start_date = get_start_date(session=session, symbol=stock_info.symbol)
        end_date = '2050-01-01'
        ## baostock获取数据
        code = exchange + '.' + symbol
        lg = bs.login()
        rs = bs.query_history_k_data_plus(code,
                                          "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,peTTM,psTTM,pcfNcfTTM,pbMRQ,isST",
                                          start_date=start_date, end_date=end_date,
                                          frequency="d", adjustflag="1")
        stock_bao_k_data = rs.get_data()

        for index, row in stock_bao_k_data.iterrows():
            stock_hist = create_stock_hist_bao_k_hfq(session=session, row=row, symbol=symbol, name=name)
            history_count += 1
        session.commit()
        bs.logout()

    return history_count


def create_part_stock_bao_k_hfq(*, session: Session, stock_offset: int = 0,
                                stock_limit: int = Query(default=1000, le=1000)) -> int:
    stock_infos_public = get_stock_infos(session=session, offset=stock_offset, limit=stock_limit)
    stock_infos = stock_infos_public.data
    history_count = create_histories_by_list(session, stock_infos)

    return history_count


def get_start_date(session, symbol) -> str:
    stock_hists = get_stock_histories(session, symbol)
    if stock_hists is None or len(stock_hists) == 0:
        return '1970-01-01'
    stock_hist = stock_hists[0][0]
    last_date = stock_hist.date
    query_start_date = last_date + datetime.timedelta(days=1)
    start_date_str = query_start_date.strftime("%Y-%m-%d")
    return start_date_str


def get_stock_histories(session, symbol):
    statement = select(StockHistoryBaoKHfq).where(StockHistoryBaoKHfq.symbol == symbol).order_by(
        StockHistoryBaoKHfq.date.desc())
    stock_hists = session.execute(statement).all()
    return stock_hists


def create_stock_hist_bao_k_hfq(session, row, symbol, name):
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
    stock_hist_bao_k_hfq_create = StockHistoryBaoKHfqCreate(code=code,
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
    db_stock_hist = StockHistoryBaoKHfq.model_validate(stock_hist_bao_k_hfq_create)
    session.add(db_stock_hist)
    # session.commit()
    # session.refresh(db_stock_hist)
    res = StockHistoryBaoKHfq.model_validate(db_stock_hist)
    return res


def empty_str_to_none(v):
    """将空值转换为none"""
    if v == '' or v is None:
        return None
    return v


def check_stock_history_date(session, check_date):
    last_trade_date = get_last_trade_date_by_date(session=session, final_date=check_date)
    statement = select(StockHistoryBaoKHfq).where(
        StockHistoryBaoKHfq.date == last_trade_date)
    items = session.execute(statement).all()
    if items is None or len(items) < 4000:
        return False
    else:
        return True
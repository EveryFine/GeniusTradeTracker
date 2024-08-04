# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_current_day_check_task
   Description :
   Author :       EveryFine
   Date：          2024/8/4
-------------------------------------------------
   Change Activity:
                   2024/8/4:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

import datetime

from sqlmodel import Session

from app.common.log import log
from app.core.db import engine
from app.crud.crud_stock_change_abnormal import check_stock_change_abnormal_date
from app.crud.crud_stock_comment import check_stock_comment_date
from app.crud.crud_stock_company_event import check_stock_company_event_date
from app.crud.crud_stock_fund_big_deal import check_stock_fund_big_deal_date
from app.crud.crud_stock_fund_concept_detail_intraday import check_stock_fund_concept_detail_intraday_date
from app.crud.crud_stock_fund_concept_detail_rank import check_stock_fund_concept_detail_rank_date
from app.crud.crud_stock_fund_concept_intraday import check_stock_fund_concept_intraday_date
from app.crud.crud_stock_fund_concept_rank import check_stock_fund_concept_rank_date
from app.crud.crud_stock_fund_industry_detail_intraday import check_stock_fund_industry_detail_intraday_date
from app.crud.crud_stock_fund_industry_detail_rank import check_stock_fund_industry_detail_rank_date
from app.crud.crud_stock_fund_industry_intraday import check_stock_fund_industry_intraday_date
from app.crud.crud_stock_fund_industry_rank import check_stock_fund_industry_rank_date
from app.crud.crud_stock_fund_market_detail import check_stock_fund_market_detail_date
from app.crud.crud_stock_fund_single_detail_intraday import check_stock_fund_single_detail_intraday_date
from app.crud.crud_stock_fund_single_detail_rank import check_stock_fund_single_detail_rank_date
from app.crud.crud_stock_fund_single_intraday import check_stock_fund_single_intraday_date
from app.crud.crud_stock_fund_single_rank import check_stock_fund_single_rank_date
from app.crud.crud_stock_history import check_stock_history_date
from app.crud.crud_stock_history_hfq import check_stock_history_hfq_date
from app.crud.crud_stock_history_qfq import check_stock_history_qfq_date
from app.crud.crud_stock_news import check_stock_news_date
from app.crud.crud_stock_pool_dt import check_stock_pool_dt_date
from app.crud.crud_stock_pool_strong import check_stock_pool_strong_date
from app.crud.crud_stock_pool_sub_new import check_stock_pool_sub_new_date
from app.crud.crud_stock_pool_zb import check_stock_pool_zb_date
from app.crud.crud_stock_pool_zt import check_stock_pool_zt_date
from app.crud.crud_stock_rank_cxd import check_stock_rank_cxd_date
from app.crud.crud_stock_rank_cxfl import check_stock_rank_cxfl_date
from app.crud.crud_stock_rank_cxg import check_stock_rank_cxg_date
from app.crud.crud_stock_rank_cxsl import check_stock_rank_cxsl_date
from app.crud.crud_stock_rank_ljqd import check_stock_rank_ljqd_date
from app.crud.crud_stock_rank_ljqs import check_stock_rank_ljqs_date
from app.crud.crud_stock_rank_lxsz import check_stock_rank_lxsz_date
from app.crud.crud_stock_rank_lxxd import check_stock_rank_lxxd_date
from app.crud.crud_stock_rank_xstp import check_stock_rank_xstp_date
from app.crud.crud_stock_rank_xxtp import check_stock_rank_xxtp_date
from app.task.stock_change_abnormal_task import execute_create_stock_change_abnormal
from app.task.stock_comment_task import execute_create_stock_comment
from app.task.stock_company_event_task import execute_create_stock_company_event
from app.task.stock_fund_big_deal_task import execute_create_stock_fund_big_deal
from app.task.stock_fund_concept_detail_intraday_task import execute_create_stock_fund_concept_detail_intraday
from app.task.stock_fund_concept_detail_rank_task import execute_create_stock_fund_concept_detail_rank
from app.task.stock_fund_concept_intraday_task import execute_create_stock_fund_concept_intraday
from app.task.stock_fund_concept_rank_task import execute_create_stock_fund_concept_rank
from app.task.stock_fund_industry_detail_intraday_task import execute_create_stock_fund_industry_detail_intraday
from app.task.stock_fund_industry_detail_rank_task import execute_create_stock_fund_industry_detail_rank
from app.task.stock_fund_industry_intraday_task import execute_create_stock_fund_industry_intraday
from app.task.stock_fund_industry_rank_task import execute_create_stock_fund_industry_rank
from app.task.stock_fund_market_detail_task import execute_create_stock_fund_market_detail
from app.task.stock_fund_single_detail_intraday_task import execute_create_stock_fund_single_detail_intraday
from app.task.stock_fund_single_detail_rank_task import execute_create_stock_fund_single_detail_rank
from app.task.stock_fund_single_intraday import execute_create_stock_fund_single_intraday
from app.task.stock_fund_single_rank_task import execute_create_stock_fund_single_rank
from app.task.stock_history_hfq_task import execute_create_stock_histories_hfq_4000_5000, \
    execute_create_stock_histories_hfq_0_1000, execute_create_stock_histories_hfq_1000_2000, \
    execute_create_stock_histories_hfq_2000_3000, execute_create_stock_histories_hfq_3000_4000
from app.task.stock_history_qfq_task import execute_create_stock_histories_qfq_4000_5000, \
    execute_create_stock_histories_qfq_3000_4000, execute_create_stock_histories_qfq_2000_3000, \
    execute_create_stock_histories_qfq_1000_2000, execute_create_stock_histories_qfq_0_1000
from app.task.stock_history_task import execute_create_stock_histories_4000_5000, \
    execute_create_stock_histories_3000_4000, execute_create_stock_histories_2000_3000, \
    execute_create_stock_histories_1000_2000, execute_create_stock_histories_0_1000
from app.task.stock_news_task import execute_create_stock_news_4000_5000, execute_create_stock_news_3000_4000, \
    execute_create_stock_news_2000_3000, execute_create_stock_news_1000_2000, execute_create_stock_news_0_1000
from app.task.stock_pool_dt_task import execute_create_stock_pool_dt
from app.task.stock_pool_strong_task import execute_create_stock_pool_strong
from app.task.stock_pool_sub_new_task import execute_create_stock_pool_sub_new
from app.task.stock_pool_zb_task import execute_create_stock_pool_zb
from app.task.stock_pool_zt_task import execute_create_stock_pool_zt
from app.task.stock_rank_cxd_task import execute_create_stock_rank_cxd
from app.task.stock_rank_cxfl_task import execute_create_stock_rank_cxfl
from app.task.stock_rank_cxg_task import execute_create_stock_rank_cxg
from app.task.stock_rank_cxsl_task import execute_create_stock_rank_cxsl
from app.task.stock_rank_ljqd_task import execute_create_stock_rank_ljqd
from app.task.stock_rank_ljqs_task import execute_create_stock_rank_ljqs
from app.task.stock_rank_lxsz_task import execute_create_stock_rank_lxsz
from app.task.stock_rank_lxxd_task import execute_create_stock_rank_lxxd
from app.task.stock_rank_xstp_task import execute_create_stock_rank_xstp
from app.task.stock_rank_xxtp_task import execute_create_stock_rank_xxtp


def execute_stock_current_day_check():
    execute_stock_change_abnormal_check()
    execute_stock_comment_check()
    execute_stock_company_event_check()
    execute_stock_fund_big_deal_check()
    execute_stock_fund_concept_detail_intraday_check()
    execute_stock_fund_concept_detail_rank_check()
    execute_stock_fund_concept_intraday_check()
    execute_stock_fund_concept_rank_check()
    execute_stock_fund_industry_detail_intraday_check()
    execute_stock_fund_industry_intraday_check()
    execute_stock_fund_industry_rank_check()
    execute_stock_fund_market_detail_check()
    execute_stock_fund_single_detail_intraday_check()
    execute_stock_fund_single_detail_rank_check()
    execute_stock_fund_single_intraday_check()
    execute_stock_pool_dt_check()
    execute_stock_pool_strong_check()
    execute_stock_pool_sub_new_check()
    execute_stock_pool_zb_check()
    execute_stock_pool_zt_check()
    execute_stock_rank_cxd_check()
    execute_stock_rank_cxfl_check()
    execute_stock_rank_cxg_check()
    execute_stock_rank_cxsl_check()
    execute_stock_rank_ljqd_check()
    execute_stock_rank_ljqs_check()
    execute_stock_rank_lxsz_check()
    execute_stock_rank_lxxd_check()
    execute_stock_rank_xstp_check()
    execute_stock_rank_xxtp_check()


def execute_stock_history_current_day_check():
    execute_stock_history_check()
    execute_stock_history_hfq_check()
    execute_stock_history_qfq_check()
    execute_stock_news_check()


def execute_stock_change_abnormal_check():
    log.info(f"{datetime.datetime.now()} check task [stock change abnormal] start")
    with Session(engine) as session:
        res = check_stock_change_abnormal_date(session, datetime.date.today())
        log.info(f"{datetime.datetime.now()} check task [stock change abnormal] end, res:{res}")
        if res is False:
            execute_create_stock_change_abnormal()


def execute_stock_comment_check():
    log.info(f"{datetime.datetime.now()} check task [stock comment] start")
    with Session(engine) as session:
        res = check_stock_comment_date(session, datetime.date.today())
        log.info(f"{datetime.datetime.now()} check task [stock comment] end, res:{res}")
        if res is False:
            execute_create_stock_comment()


def execute_stock_company_event_check():
    log.info(f"{datetime.datetime.now()} check task [stock company event] start")
    with Session(engine) as session:
        res = check_stock_company_event_date(session, datetime.date.today())
        log.info(f"{datetime.datetime.now()} check task [stock company event] end, res:{res}")
        if res is False:
            execute_create_stock_company_event()


def execute_stock_fund_big_deal_check():
    log.info(f"{datetime.datetime.now()} check task [stock fund bid deal] start")
    with Session(engine) as session:
        res = check_stock_fund_big_deal_date(session, datetime.date.today())
        log.info(f"{datetime.datetime.now()} check task [stock fund bid deal] end, res:{res}")
        if res is False:
            execute_create_stock_fund_big_deal()


def execute_stock_fund_concept_detail_intraday_check():
    log.info(f"{datetime.datetime.now()} check task [stock fund concept detail intraday] start")
    with Session(engine) as session:
        res = check_stock_fund_concept_detail_intraday_date(session, datetime.date.today())
        log.info(f"{datetime.datetime.now()} check task [stock fund concept detail intraday] end, res:{res}")
        if res is False:
            execute_create_stock_fund_concept_detail_intraday()


# check_stock_fund_concept_detail_rank_date

def execute_stock_fund_concept_detail_rank_check():
    log.info(f"{datetime.datetime.now()} check task [stock fund concept detail rank] start")
    with Session(engine) as session:
        res = check_stock_fund_concept_detail_rank_date(session, datetime.date.today())
        log.info(f"{datetime.datetime.now()} check task [stock fund concept detail rank] end, res:{res}")
        if res is False:
            execute_create_stock_fund_concept_detail_rank()


def execute_stock_fund_concept_intraday_check():
    log.info(f"{datetime.datetime.now()} check task [stock fund concept intraday] start")
    with Session(engine) as session:
        res = check_stock_fund_concept_intraday_date(session, datetime.date.today())
        log.info(f"{datetime.datetime.now()} check task [stock fund concept intraday] end, res:{res}")
        if res is False:
            execute_create_stock_fund_concept_intraday()


def execute_stock_fund_concept_rank_check():
    log.info(f"{datetime.datetime.now()} check task [stock fund concept rank] start")
    with Session(engine) as session:
        res = check_stock_fund_concept_rank_date(session, datetime.date.today())
        log.info(f"{datetime.datetime.now()} check task [stock fund concept rank] end, res:{res}")
        if res is False:
            execute_create_stock_fund_concept_rank()


def execute_stock_fund_industry_detail_intraday_check():
    log.info(f"{datetime.datetime.now()} check task [stock fund industry detail intraday] start")
    with Session(engine) as session:
        res = check_stock_fund_industry_detail_intraday_date(session, datetime.date.today())
        log.info(f"{datetime.datetime.now()} check task [stock fund industry detail intraday] end, res:{res}")
        if res is False:
            execute_create_stock_fund_industry_detail_intraday()


def execute_stock_fund_industry_detail_rank_check():
    log.info(f"{datetime.datetime.now()} check task [stock fund industry detail rank] start")
    with Session(engine) as session:
        res = check_stock_fund_industry_detail_rank_date(session, datetime.date.today())
        log.info(f"{datetime.datetime.now()} check task [stock fund industry detail rank] end, res:{res}")
        if res is False:
            execute_create_stock_fund_industry_detail_rank()


def execute_stock_fund_industry_intraday_check():
    log.info(f"{datetime.datetime.now()} check task [stock_fund_industry_intraday] start")
    with Session(engine) as session:
        res = check_stock_fund_industry_intraday_date(session, datetime.date.today())
        log.info(f"{datetime.datetime.now()} check task [stock_fund_industry_intraday] end, res:{res}")
        if res is False:
            execute_create_stock_fund_industry_intraday()


def execute_stock_fund_industry_rank_check():
    log.info(f"{datetime.datetime.now()} check task [stock_fund_industry_rank] start")
    with Session(engine) as session:
        res = check_stock_fund_industry_rank_date(session, datetime.date.today())
        log.info(f"{datetime.datetime.now()} check task [stock_fund_industry_rank] end, res:{res}")
        if res is False:
            execute_create_stock_fund_industry_rank()


def execute_stock_fund_market_detail_check():
    log.info(f"{datetime.datetime.now()} check task [stock_fund_market_detail] start")
    with Session(engine) as session:
        res = check_stock_fund_market_detail_date(session, datetime.date.today())
        log.info(f"{datetime.datetime.now()} check task [stock_fund_market_detail] end, res:{res}")
        if res is False:
            execute_create_stock_fund_market_detail()


def execute_stock_fund_single_detail_intraday_check():
    log.info(f"{datetime.datetime.now()} check task [stock_fund_single_detail_intraday] start")
    with Session(engine) as session:
        res = check_stock_fund_single_detail_intraday_date(session, datetime.date.today())
        log.info(f"{datetime.datetime.now()} check task [stock_fund_single_detail_intraday] end, res:{res}")
        if res is False:
            execute_create_stock_fund_single_detail_intraday()


def execute_stock_fund_single_detail_rank_check():
    log.info(f"{datetime.datetime.now()} check task [stock_fund_single_detail_rank] start")
    with Session(engine) as session:
        res = check_stock_fund_single_detail_rank_date(session, datetime.date.today())
        log.info(f"{datetime.datetime.now()} check task [stock_fund_single_detail_rank] end, res:{res}")
        if res is False:
            execute_create_stock_fund_single_detail_rank()


def execute_stock_fund_single_intraday_check():
    log.info(f"{datetime.datetime.now()} check task [stock_fund_single_intraday] start")
    with Session(engine) as session:
        res = check_stock_fund_single_intraday_date(session, datetime.date.today())
        log.info(f"{datetime.datetime.now()} check task [stock_fund_single_intraday] end, res:{res}")
        if res is False:
            execute_create_stock_fund_single_intraday()


def execute_stock_fund_single_rank_check():
    log.info(f"{datetime.datetime.now()} check task [stock_fund_single_rank] start")
    with Session(engine) as session:
        res = check_stock_fund_single_rank_date(session, datetime.date.today())
        log.info(f"{datetime.datetime.now()} check task [stock_fund_single_rank] end, res:{res}")
        if res is False:
            execute_create_stock_fund_single_rank()


def execute_stock_history_check():
    log.info(f"{datetime.datetime.now()} check task [stock_history] start")
    with Session(engine) as session:
        res = check_stock_history_date(session, datetime.date.today())
        log.info(f"{datetime.datetime.now()} check task [stock_history] end, res:{res}")
        if res is False:
            execute_create_stock_histories_4000_5000()
            execute_create_stock_histories_3000_4000()
            execute_create_stock_histories_2000_3000()
            execute_create_stock_histories_1000_2000()
            execute_create_stock_histories_0_1000()


def execute_stock_history_hfq_check():
    log.info(f"{datetime.datetime.now()} check task [stock_history_hfq] start")
    with Session(engine) as session:
        res = check_stock_history_hfq_date(session, datetime.date.today())
        log.info(f"{datetime.datetime.now()} check task [stock_history_hfq] end, res:{res}")
        if res is False:
            execute_create_stock_histories_hfq_4000_5000()
            execute_create_stock_histories_hfq_3000_4000()
            execute_create_stock_histories_hfq_2000_3000()
            execute_create_stock_histories_hfq_1000_2000()
            execute_create_stock_histories_hfq_0_1000()


def execute_stock_history_qfq_check():
    log.info(f"{datetime.datetime.now()} check task [stock_history_qfq] start")
    with Session(engine) as session:
        res = check_stock_history_qfq_date(session, datetime.date.today())
        log.info(f"{datetime.datetime.now()} check task [stock_history_qfq] end, res:{res}")
        if res is False:
            execute_create_stock_histories_qfq_4000_5000()
            execute_create_stock_histories_qfq_3000_4000()
            execute_create_stock_histories_qfq_2000_3000()
            execute_create_stock_histories_qfq_1000_2000()
            execute_create_stock_histories_qfq_0_1000()


def execute_stock_news_check():
    log.info(f"{datetime.datetime.now()} check task [stock_news] start")
    with Session(engine) as session:
        res = check_stock_news_date(session, datetime.date.today())
        log.info(f"{datetime.datetime.now()} check task [stock_news] end, res:{res}")
        if res is False:
            execute_create_stock_news_4000_5000()
            execute_create_stock_news_3000_4000()
            execute_create_stock_news_2000_3000()
            execute_create_stock_news_1000_2000()
            execute_create_stock_news_0_1000()


def execute_stock_pool_dt_check():
    log.info(f"{datetime.datetime.now()} check task [stock_pool_dt] start")
    with Session(engine) as session:
        res = check_stock_pool_dt_date(session, datetime.date.today())
        log.info(f"{datetime.datetime.now()} check task [stock_pool_dt] end, res:{res}")
        if res is False:
            execute_create_stock_pool_dt()


def execute_stock_pool_strong_check():
    log.info(f"{datetime.datetime.now()} check task [stock_pool_strong] start")
    with Session(engine) as session:
        res = check_stock_pool_strong_date(session, datetime.date.today())
        log.info(f"{datetime.datetime.now()} check task [stock_pool_strong] end, res:{res}")
        if res is False:
            execute_create_stock_pool_strong()


def execute_stock_pool_sub_new_check():
    log.info(f"{datetime.datetime.now()} check task [stock_pool_sub_new] start")
    with Session(engine) as session:
        res = check_stock_pool_sub_new_date(session, datetime.date.today())
        log.info(f"{datetime.datetime.now()} check task [stock_pool_sub_new] end, res:{res}")
        if res is False:
            execute_create_stock_pool_sub_new()


def execute_stock_pool_zb_check():
    log.info(f"{datetime.datetime.now()} check task [stock_pool_zb] start")
    with Session(engine) as session:
        res = check_stock_pool_zb_date(session, datetime.date.today())
        log.info(f"{datetime.datetime.now()} check task [stock_pool_zb] end, res:{res}")
        if res is False:
            execute_create_stock_pool_zb()


def execute_stock_pool_zt_check():
    log.info(f"{datetime.datetime.now()} check task [stock_pool_zt] start")
    with Session(engine) as session:
        res = check_stock_pool_zt_date(session, datetime.date.today())
        log.info(f"{datetime.datetime.now()} check task [stock_pool_zt] end, res:{res}")
        if res is False:
            execute_create_stock_pool_zt()


def execute_stock_rank_cxd_check():
    log.info(f"{datetime.datetime.now()} check task [stock_rank_cxd] start")
    with Session(engine) as session:
        res = check_stock_rank_cxd_date(session, datetime.date.today())
        log.info(f"{datetime.datetime.now()} check task [stock_rank_cxd] end, res:{res}")
        if res is False:
            execute_create_stock_rank_cxd()


def execute_stock_rank_cxfl_check():
    log.info(f"{datetime.datetime.now()} check task [stock_rank_cxfl] start")
    with Session(engine) as session:
        res = check_stock_rank_cxfl_date(session, datetime.date.today())
        log.info(f"{datetime.datetime.now()} check task [stock_rank_cxfl] end, res:{res}")
        if res is False:
            execute_create_stock_rank_cxfl()


def execute_stock_rank_cxg_check():
    log.info(f"{datetime.datetime.now()} check task [stock_rank_cxg] start")
    with Session(engine) as session:
        res = check_stock_rank_cxg_date(session, datetime.date.today())
        log.info(f"{datetime.datetime.now()} check task [stock_rank_cxg] end, res:{res}")
        if res is False:
            execute_create_stock_rank_cxg()


def execute_stock_rank_cxsl_check():
    log.info(f"{datetime.datetime.now()} check task [stock_rank_cxsl] start")
    with Session(engine) as session:
        res = check_stock_rank_cxsl_date(session, datetime.date.today())
        log.info(f"{datetime.datetime.now()} check task [stock_rank_cxsl] end, res:{res}")
        if res is False:
            execute_create_stock_rank_cxsl()


def execute_stock_rank_ljqd_check():
    log.info(f"{datetime.datetime.now()} check task [stock_rank_ljqd] start")
    with Session(engine) as session:
        res = check_stock_rank_ljqd_date(session, datetime.date.today())
        log.info(f"{datetime.datetime.now()} check task [stock_rank_ljqd] end, res:{res}")
        if res is False:
            execute_create_stock_rank_ljqd()


def execute_stock_rank_ljqs_check():
    log.info(f"{datetime.datetime.now()} check task [stock_rank_ljqs] start")
    with Session(engine) as session:
        res = check_stock_rank_ljqs_date(session, datetime.date.today())
        log.info(f"{datetime.datetime.now()} check task [stock_rank_ljqs] end, res:{res}")
        if res is False:
            execute_create_stock_rank_ljqs()


def execute_stock_rank_lxsz_check():
    log.info(f"{datetime.datetime.now()} check task [stock_rank_lxsz] start")
    with Session(engine) as session:
        res = check_stock_rank_lxsz_date(session, datetime.date.today())
        log.info(f"{datetime.datetime.now()} check task [stock_rank_lxsz] end, res:{res}")
        if res is False:
            execute_create_stock_rank_lxsz()

def execute_stock_rank_lxxd_check():
    log.info(f"{datetime.datetime.now()} check task [stock_rank_lxxd] start")
    with Session(engine) as session:
        res = check_stock_rank_lxxd_date(session, datetime.date.today())
        log.info(f"{datetime.datetime.now()} check task [stock_rank_lxxd] end, res:{res}")
        if res is False:
            execute_create_stock_rank_lxxd()

def execute_stock_rank_xstp_check():
    log.info(f"{datetime.datetime.now()} check task [stock_rank_xstp] start")
    with Session(engine) as session:
        res = check_stock_rank_xstp_date(session, datetime.date.today())
        log.info(f"{datetime.datetime.now()} check task [stock_rank_xstp] end, res:{res}")
        if res is False:
            execute_create_stock_rank_xstp()

def execute_stock_rank_xxtp_check():
    log.info(f"{datetime.datetime.now()} check task [stock_rank_xxtp] start")
    with Session(engine) as session:
        res = check_stock_rank_xxtp_date(session, datetime.date.today())
        log.info(f"{datetime.datetime.now()} check task [stock_rank_xxtp] end, res:{res}")
        if res is False:
            execute_create_stock_rank_xxtp()
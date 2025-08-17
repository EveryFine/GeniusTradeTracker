# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     main
   Description :
   Author :       EveryFine
   Date：          2024/6/22
-------------------------------------------------
   Change Activity:
                   2024/6/22:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

import socket
from pathlib import Path

import uvicorn
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.background import BackgroundScheduler
from sqlmodel import SQLModel

from app.common.log import log
from app.core.conf import settings
from app.core.db import engine
from app.core.register import register_app
from app.task.stock_change_abnormal_task import execute_create_stock_change_abnormal
from app.task.stock_comment_task import execute_create_stock_comment
from app.task.stock_company_event_task import execute_create_stock_company_event
from app.task.stock_current_day_check_task import execute_stock_current_day_check, \
    execute_stock_history_current_day_check
from app.task.stock_cyq_em_task import execute_create_stock_cyq_em_0_1000, execute_create_stock_cyq_em_1000_2000, \
    execute_create_stock_cyq_em_2000_3000, execute_create_stock_cyq_em_3000_4000, execute_create_stock_cyq_em_4000_5000
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
from app.task.stock_fund_single_detail_realtime_task import execute_create_stock_fund_single_detail_realtime
from app.task.stock_fund_single_intraday import execute_create_stock_fund_single_intraday
from app.task.stock_fund_single_rank_task import execute_create_stock_fund_single_rank
from app.task.stock_history_bao_k_hfq_task import execute_create_stock_history_bao_k_hfq_0_1000, \
    execute_create_stock_history_bao_k_hfq_1000_2000, execute_create_stock_history_bao_k_hfq_2000_3000, \
    execute_create_stock_history_bao_k_hfq_3000_4000, execute_create_stock_history_bao_k_hfq_4000_5000
from app.task.stock_history_bao_k_qfq_task import execute_create_stock_history_bao_k_qfq_0_1000, \
    execute_create_stock_history_bao_k_qfq_1000_2000, execute_create_stock_history_bao_k_qfq_2000_3000, \
    execute_create_stock_history_bao_k_qfq_3000_4000, execute_create_stock_history_bao_k_qfq_4000_5000
from app.task.stock_history_bao_k_task import execute_create_stock_history_bao_k_0_1000, \
    execute_create_stock_history_bao_k_1000_2000, execute_create_stock_history_bao_k_2000_3000, \
    execute_create_stock_history_bao_k_3000_4000, execute_create_stock_history_bao_k_4000_5000
from app.task.stock_history_hfq_task import execute_create_stock_histories_hfq_0_1000, \
    execute_create_stock_histories_hfq_1000_2000, execute_create_stock_histories_hfq_2000_3000, \
    execute_create_stock_histories_hfq_3000_4000, execute_create_stock_histories_hfq_4000_5000
from app.task.stock_history_qfq_task import execute_create_stock_histories_qfq_0_1000, \
    execute_create_stock_histories_qfq_1000_2000, execute_create_stock_histories_qfq_3000_4000, \
    execute_create_stock_histories_qfq_2000_3000, execute_create_stock_histories_qfq_4000_5000
from app.task.stock_history_task import execute_create_stock_histories_0_1000, execute_create_stock_histories_1000_2000, \
    execute_create_stock_histories_2000_3000, execute_create_stock_histories_3000_4000, \
    execute_create_stock_histories_4000_5000
from app.task.stock_lhb_detail_em_task import execute_create_stock_lhb_detail_em
from app.task.stock_lhb_hyyyb_em_task import execute_create_stock_lhb_hyyyb_em
from app.task.stock_lhb_yyb_detail_em_task import execute_create_stock_lhb_yyb_detail_em
from app.task.stock_news_task import execute_create_stock_news_0_1000, execute_create_stock_news_1000_2000, \
    execute_create_stock_news_2000_3000, execute_create_stock_news_3000_4000, execute_create_stock_news_4000_5000

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
from app.task.stock_rank_xzjp_task import execute_create_stock_rank_xzjp
from app.task.stock_zh_a_spot_em_realtime_task import execute_create_stock_zh_a_spot_em_realtime

app = register_app()

jobstores = {
    'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
}
scheduler = BackgroundScheduler(jobstores=jobstores)


def init_scheduler():
    # # 历史行情 - 不复权
    scheduler.add_job(execute_create_stock_histories_0_1000, 'cron', hour=17, minute=0, second=0)
    scheduler.add_job(execute_create_stock_histories_1000_2000, 'cron', hour=17, minute=20, second=0)
    scheduler.add_job(execute_create_stock_histories_2000_3000, 'cron', hour=17, minute=40, second=0)
    scheduler.add_job(execute_create_stock_histories_3000_4000, 'cron', hour=18, minute=0, second=0)
    scheduler.add_job(execute_create_stock_histories_4000_5000, 'cron', hour=18, minute=20, second=0)
    #
    scheduler.add_job(execute_create_stock_histories_0_1000, 'cron', hour=23, minute=30, second=0)
    scheduler.add_job(execute_create_stock_histories_1000_2000, 'cron', hour=23, minute=15, second=0)
    scheduler.add_job(execute_create_stock_histories_2000_3000, 'cron', hour=23, minute=30, second=0)
    scheduler.add_job(execute_create_stock_histories_3000_4000, 'cron', hour=23, minute=45, second=0)
    scheduler.add_job(execute_create_stock_histories_4000_5000, 'cron', hour=23, minute=0, second=0)
    #
    # # 历史行情 - 前复权
    # scheduler.add_job(execute_create_stock_histories_qfq_0_1000, 'cron', hour=18, minute=15, second=0)
    # scheduler.add_job(execute_create_stock_histories_qfq_1000_2000, 'cron', hour=18, minute=45, second=0)
    # scheduler.add_job(execute_create_stock_histories_qfq_2000_3000, 'cron', hour=19, minute=15, second=0)
    # scheduler.add_job(execute_create_stock_histories_qfq_3000_4000, 'cron', hour=19, minute=45, second=0)
    # scheduler.add_job(execute_create_stock_histories_qfq_4000_5000, 'cron', hour=20, minute=15, second=0)
    #
    # # scheduler.add_job(execute_create_stock_histories_qfq_0_1000, 'cron', hour=21, minute=25, second=0)
    # # scheduler.add_job(execute_create_stock_histories_qfq_1000_2000, 'cron', hour=21, minute=21, second=0)
    # # scheduler.add_job(execute_create_stock_histories_qfq_2000_3000, 'cron', hour=21, minute=20, second=0)
    # # scheduler.add_job(execute_create_stock_histories_qfq_3000_4000, 'cron', hour=21, minute=30, second=0)
    # # scheduler.add_job(execute_create_stock_histories_qfq_4000_5000, 'cron', hour=21, minute=40, second=0)
    #
    # # 历史行情 - 后复权
    # scheduler.add_job(execute_create_stock_histories_hfq_0_1000, 'cron', hour=17, minute=40, second=0)
    # scheduler.add_job(execute_create_stock_histories_hfq_1000_2000, 'cron', hour=18, minute=10, second=0)
    # scheduler.add_job(execute_create_stock_histories_hfq_2000_3000, 'cron', hour=18, minute=40, second=0)
    # scheduler.add_job(execute_create_stock_histories_hfq_3000_4000, 'cron', hour=19, minute=10, second=0)
    # scheduler.add_job(execute_create_stock_histories_hfq_4000_5000, 'cron', hour=19, minute=40, second=0)

    # scheduler.add_job(execute_create_stock_histories_hfq_0_1000, 'cron', hour=21, minute=25, second=0)
    # scheduler.add_job(execute_create_stock_histories_hfq_1000_2000, 'cron', hour=21, minute=12, second=0)
    # scheduler.add_job(execute_create_stock_histories_hfq_2000_3000, 'cron', hour=21, minute=22, second=0)
    # scheduler.add_job(execute_create_stock_histories_hfq_3000_4000, 'cron', hour=21, minute=33, second=0)
    # scheduler.add_job(execute_create_stock_histories_hfq_4000_5000, 'cron', hour=21, minute=44, second=0)

    # 历史行情 - BaoStock 不复权
    scheduler.add_job(execute_create_stock_history_bao_k_0_1000, 'cron', hour=23, minute=15, second=0)
    scheduler.add_job(execute_create_stock_history_bao_k_1000_2000, 'cron', hour=1, minute=30, second=0)
    scheduler.add_job(execute_create_stock_history_bao_k_2000_3000, 'cron', hour=3, minute=30, second=0)
    scheduler.add_job(execute_create_stock_history_bao_k_3000_4000, 'cron', hour=5, minute=30, second=0)
    scheduler.add_job(execute_create_stock_history_bao_k_4000_5000, 'cron', hour=7, minute=30, second=0)

    # 历史行情 - BaoStock 前复权
    # scheduler.add_job(execute_create_stock_history_bao_k_qfq_0_1000, 'cron', hour=18, minute=11, second=0)
    # scheduler.add_job(execute_create_stock_history_bao_k_qfq_1000_2000, 'cron', hour=20, minute=11, second=0)
    # scheduler.add_job(execute_create_stock_history_bao_k_qfq_2000_3000, 'cron', hour=22, minute=11, second=0)
    # scheduler.add_job(execute_create_stock_history_bao_k_qfq_3000_4000, 'cron', hour=0, minute=11, second=0)
    # scheduler.add_job(execute_create_stock_history_bao_k_qfq_4000_5000, 'cron', hour=2, minute=11, second=0)

    # 历史行情 - BaoStock 后复权
    # scheduler.add_job(execute_create_stock_history_bao_k_hfq_0_1000, 'cron', hour=4, minute=11, second=0)
    # scheduler.add_job(execute_create_stock_history_bao_k_hfq_1000_2000, 'cron', hour=6, minute=11, second=0)
    # scheduler.add_job(execute_create_stock_history_bao_k_hfq_2000_3000, 'cron', hour=9, minute=11, second=0)
    # scheduler.add_job(execute_create_stock_history_bao_k_hfq_3000_4000, 'cron', hour=11, minute=11, second=0)
    # scheduler.add_job(execute_create_stock_history_bao_k_hfq_4000_5000, 'cron', hour=13, minute=11, second=0)

    # 公司新闻
    scheduler.add_job(execute_create_stock_news_0_1000, 'cron', hour=17, minute=0, second=0)
    scheduler.add_job(execute_create_stock_news_1000_2000, 'cron', hour=17, minute=15, second=0)
    scheduler.add_job(execute_create_stock_news_2000_3000, 'cron', hour=17, minute=30, second=0)
    scheduler.add_job(execute_create_stock_news_3000_4000, 'cron', hour=17, minute=45, second=0)
    scheduler.add_job(execute_create_stock_news_4000_5000, 'cron', hour=18, minute=0, second=0)

    scheduler.add_job(execute_create_stock_news_0_1000, 'cron', hour=22, minute=0, second=0)
    scheduler.add_job(execute_create_stock_news_1000_2000, 'cron', hour=21, minute=35, second=0)
    scheduler.add_job(execute_create_stock_news_2000_3000, 'cron', hour=21, minute=30, second=0)
    scheduler.add_job(execute_create_stock_news_3000_4000, 'cron', hour=21, minute=45, second=0)
    scheduler.add_job(execute_create_stock_news_4000_5000, 'cron', hour=22, minute=0, second=0)

    # 筹码分布
    scheduler.add_job(execute_create_stock_cyq_em_0_1000, 'cron', hour=8, minute=2, second=0)
    scheduler.add_job(execute_create_stock_cyq_em_1000_2000, 'cron', hour=9, minute=12, second=0)
    scheduler.add_job(execute_create_stock_cyq_em_2000_3000, 'cron', hour=10, minute=22, second=0)
    scheduler.add_job(execute_create_stock_cyq_em_3000_4000, 'cron', hour=11, minute=32, second=0)
    scheduler.add_job(execute_create_stock_cyq_em_4000_5000, 'cron', hour=12, minute=42, second=0)

    scheduler.add_job(execute_create_stock_cyq_em_0_1000, 'cron', hour=22, minute=2, second=0)
    scheduler.add_job(execute_create_stock_cyq_em_1000_2000, 'cron', hour=23, minute=12, second=0)
    scheduler.add_job(execute_create_stock_cyq_em_2000_3000, 'cron', hour=1, minute=22, second=0)
    scheduler.add_job(execute_create_stock_cyq_em_3000_4000, 'cron', hour=2, minute=32, second=0)
    scheduler.add_job(execute_create_stock_cyq_em_4000_5000, 'cron', hour=3, minute=42, second=0)

    # 盘口异动
    scheduler.add_job(execute_create_stock_change_abnormal, 'cron', hour=18, minute=15, second=0)
    scheduler.add_job(execute_create_stock_change_abnormal, 'cron', hour=19, minute=10, second=0)

    scheduler.add_job(execute_create_stock_change_abnormal, 'cron', hour=22, minute=10, second=0)

    # 千股千评
    scheduler.add_job(execute_create_stock_comment, 'cron', hour=18, minute=46, second=0)
    scheduler.add_job(execute_create_stock_comment, 'cron', hour=19, minute=21, second=0)

    scheduler.add_job(execute_create_stock_comment, 'cron', hour=22, minute=21, second=0)

    # 公司动态
    scheduler.add_job(execute_create_stock_company_event, 'cron', hour=19, minute=5, second=0)

    scheduler.add_job(execute_create_stock_company_event, 'cron', hour=22, minute=5, second=0)

    # 技术指标--创新高
    scheduler.add_job(execute_create_stock_rank_cxg, 'cron', hour=18, minute=10, second=0)
    scheduler.add_job(execute_create_stock_rank_cxg, 'cron', hour=21, minute=12, second=0)

    scheduler.add_job(execute_create_stock_rank_cxg, 'cron', hour=22, minute=12, second=0)

    # 技术指标--创新低
    scheduler.add_job(execute_create_stock_rank_cxd, 'cron', hour=19, minute=33, second=0)
    scheduler.add_job(execute_create_stock_rank_cxd, 'cron', hour=21, minute=22, second=0)

    scheduler.add_job(execute_create_stock_rank_cxd, 'cron', hour=22, minute=22, second=0)

    # 技术指标--连续上涨
    scheduler.add_job(execute_create_stock_rank_lxsz, 'cron', hour=18, minute=40, second=0)
    scheduler.add_job(execute_create_stock_rank_lxsz, 'cron', hour=21, minute=29, second=0)

    # 技术指标--连续下跌
    scheduler.add_job(execute_create_stock_rank_lxxd, 'cron', hour=18, minute=52, second=0)
    scheduler.add_job(execute_create_stock_rank_lxxd, 'cron', hour=20, minute=38, second=0)

    scheduler.add_job(execute_create_stock_rank_lxxd, 'cron', hour=21, minute=38, second=0)

    # 技术指标--持续放量
    scheduler.add_job(execute_create_stock_rank_cxfl, 'cron', hour=18, minute=43, second=0)
    scheduler.add_job(execute_create_stock_rank_cxfl, 'cron', hour=21, minute=12, second=0)

    scheduler.add_job(execute_create_stock_rank_cxfl, 'cron', hour=22, minute=12, second=0)

    # 技术指标--持续缩量
    scheduler.add_job(execute_create_stock_rank_cxsl, 'cron', hour=17, minute=47, second=0)
    scheduler.add_job(execute_create_stock_rank_cxsl, 'cron', hour=20, minute=23, second=0)

    scheduler.add_job(execute_create_stock_rank_cxsl, 'cron', hour=22, minute=23, second=0)

    # 技术指标--向上突破
    scheduler.add_job(execute_create_stock_rank_xstp, 'cron', hour=18, minute=26, second=0)
    scheduler.add_job(execute_create_stock_rank_xstp, 'cron', hour=19, minute=46, second=0)

    scheduler.add_job(execute_create_stock_rank_xstp, 'cron', hour=21, minute=46, second=0)

    # 技术指标--向下突破
    scheduler.add_job(execute_create_stock_rank_xxtp, 'cron', hour=18, minute=48, second=0)
    scheduler.add_job(execute_create_stock_rank_xxtp, 'cron', hour=19, minute=36, second=0)

    scheduler.add_job(execute_create_stock_rank_xxtp, 'cron', hour=21, minute=36, second=0)

    # 技术指标--量价齐升
    scheduler.add_job(execute_create_stock_rank_ljqs, 'cron', hour=18, minute=10, second=0)
    scheduler.add_job(execute_create_stock_rank_ljqs, 'cron', hour=20, minute=17, second=0)

    scheduler.add_job(execute_create_stock_rank_ljqs, 'cron', hour=22, minute=17, second=0)

    # 技术指标--量价齐跌
    scheduler.add_job(execute_create_stock_rank_ljqd, 'cron', hour=18, minute=15, second=0)
    scheduler.add_job(execute_create_stock_rank_ljqd, 'cron', hour=21, minute=11, second=0)

    scheduler.add_job(execute_create_stock_rank_ljqd, 'cron', hour=22, minute=11, second=0)

    # 技术指标--险资举牌
    scheduler.add_job(execute_create_stock_rank_xzjp, 'cron', hour=19, minute=5, second=0)
    scheduler.add_job(execute_create_stock_rank_xzjp, 'cron', hour=21, minute=12, second=0)

    # 资金流--个股--即时
    scheduler.add_job(execute_create_stock_fund_single_intraday, 'cron', hour=16, minute=13, second=0)
    scheduler.add_job(execute_create_stock_fund_single_intraday, 'cron', hour=19, minute=13, second=0)
    scheduler.add_job(execute_create_stock_fund_single_intraday, 'cron', hour=20, minute=22, second=0)

    scheduler.add_job(execute_create_stock_fund_single_intraday, 'cron', hour=22, minute=22, second=0)

    # 资金流--个股--排行
    scheduler.add_job(execute_create_stock_fund_single_rank, 'cron', hour=16, minute=24, second=0)
    scheduler.add_job(execute_create_stock_fund_single_rank, 'cron', hour=21, minute=16, second=0)
    scheduler.add_job(execute_create_stock_fund_single_rank, 'cron', hour=19, minute=24, second=0)

    scheduler.add_job(execute_create_stock_fund_single_rank, 'cron', hour=22, minute=24, second=0)

    # 资金流--概念--即时
    scheduler.add_job(execute_create_stock_fund_concept_intraday, 'cron', hour=16, minute=11, second=0)
    scheduler.add_job(execute_create_stock_fund_concept_intraday, 'cron', hour=18, minute=11, second=0)
    scheduler.add_job(execute_create_stock_fund_concept_intraday, 'cron', hour=21, minute=23, second=0)

    scheduler.add_job(execute_create_stock_fund_concept_intraday, 'cron', hour=22, minute=23, second=0)

    # 资金流--概念--排行
    scheduler.add_job(execute_create_stock_fund_concept_rank, 'cron', hour=16, minute=13, second=0)
    scheduler.add_job(execute_create_stock_fund_concept_rank, 'cron', hour=19, minute=13, second=0)
    scheduler.add_job(execute_create_stock_fund_concept_rank, 'cron', hour=21, minute=34, second=0)

    scheduler.add_job(execute_create_stock_fund_concept_rank, 'cron', hour=22, minute=34, second=0)

    # 资金流--行业--即时
    scheduler.add_job(execute_create_stock_fund_industry_intraday, 'cron', hour=16, minute=26, second=0)
    scheduler.add_job(execute_create_stock_fund_industry_intraday, 'cron', hour=21, minute=18, second=0)
    scheduler.add_job(execute_create_stock_fund_industry_intraday, 'cron', hour=19, minute=26, second=0)

    scheduler.add_job(execute_create_stock_fund_industry_intraday, 'cron', hour=22, minute=46, second=0)

    # 资金流--行业--排行
    scheduler.add_job(execute_create_stock_fund_industry_rank, 'cron', hour=16, minute=35, second=0)
    scheduler.add_job(execute_create_stock_fund_industry_rank, 'cron', hour=21, minute=22, second=0)
    scheduler.add_job(execute_create_stock_fund_industry_rank, 'cron', hour=18, minute=35, second=0)

    scheduler.add_job(execute_create_stock_fund_industry_rank, 'cron', hour=22, minute=22, second=0)

    # 资金流--大单追踪
    scheduler.add_job(execute_create_stock_fund_big_deal, 'cron', hour=16, minute=22, second=0)
    scheduler.add_job(execute_create_stock_fund_big_deal, 'cron', hour=20, minute=16, second=0)
    scheduler.add_job(execute_create_stock_fund_big_deal, 'cron', hour=18, minute=22, second=0)

    scheduler.add_job(execute_create_stock_fund_big_deal, 'cron', hour=22, minute=22, second=0)
    # 资金流--个股--详细--盘中实时
    # 开盘执行
    scheduler.add_job(
        execute_create_stock_fund_single_detail_realtime,
        'cron',
        hour=9,
        minute=30,
        second=30,
        day_of_week='mon,tue,wed,thu,fri'
    )
    # 收盘执行
    scheduler.add_job(
        execute_create_stock_fund_single_detail_realtime,
        'cron',
        hour=14,
        minute=50,
        second=10,
        day_of_week='mon,tue,wed,thu,fri'
    )

    # 10:00～11:30, 13:00~15:00每10分钟执行一次
    # scheduler.add_job(
    #     execute_create_stock_fund_single_detail_realtime,
    #     'cron',
    #     hour='10,13,14',
    #     minute='0,10,20,30,40,50',
    #     second=0
    # )
    # scheduler.add_job(
    #     execute_create_stock_fund_single_detail_realtime,
    #     'cron',
    #     hour=11,
    #     minute='0,10,20,30',
    #     second=0
    # )
    # 实时行情数据--东财--沪深京A股
    # 开盘执行
    # day of week: sun,mon,tue,wed,thu,fri,sat
    # 所以一周的英文简写依次为：
    # 周一：mon
    # 周二：tue
    # 周三：wed
    # 周四：thu
    # 周五：fri
    # 周六：sat
    # 周日：sun
    scheduler.add_job(
        execute_create_stock_zh_a_spot_em_realtime,
        'cron',
        hour=9,
        minute=30,
        second=30,
        day_of_week='mon,tue,wed,thu,fri'
    )
    # 收盘执行
    scheduler.add_job(
        execute_create_stock_zh_a_spot_em_realtime,
        'cron',
        hour=14,
        minute=50,
        second=10,
        day_of_week='mon,tue,wed,thu,fri'
    )
    # 资金流--个股--详细--即时
    scheduler.add_job(execute_create_stock_fund_single_detail_intraday, 'cron', hour=16, minute=17, second=0)
    scheduler.add_job(execute_create_stock_fund_single_detail_intraday, 'cron', hour=17, minute=17, second=0)
    scheduler.add_job(execute_create_stock_fund_single_detail_intraday, 'cron', hour=19, minute=17, second=0)
    scheduler.add_job(execute_create_stock_fund_single_detail_intraday, 'cron', hour=21, minute=36, second=0)

    scheduler.add_job(execute_create_stock_fund_single_detail_intraday, 'cron', hour=22, minute=36, second=0)

    # 资金流--个股--详细--排名
    scheduler.add_job(execute_create_stock_fund_single_detail_rank, 'cron', hour=16, minute=27, second=0)
    scheduler.add_job(execute_create_stock_fund_single_detail_rank, 'cron', hour=17, minute=27, second=0)
    scheduler.add_job(execute_create_stock_fund_single_detail_rank, 'cron', hour=19, minute=27, second=0)
    scheduler.add_job(execute_create_stock_fund_single_detail_rank, 'cron', hour=20, minute=46, second=0)

    scheduler.add_job(execute_create_stock_fund_single_detail_rank, 'cron', hour=21, minute=46, second=0)

    # 资金流--大盘
    scheduler.add_job(execute_create_stock_fund_market_detail, 'cron', hour=16, minute=52, second=0)
    scheduler.add_job(execute_create_stock_fund_market_detail, 'cron', hour=18, minute=52, second=0)
    scheduler.add_job(execute_create_stock_fund_market_detail, 'cron', hour=20, minute=52, second=0)

    scheduler.add_job(execute_create_stock_fund_market_detail, 'cron', hour=21, minute=52, second=0)

    # 资金流--行业--详细--即时
    scheduler.add_job(execute_create_stock_fund_industry_detail_intraday, 'cron', hour=17, minute=38, second=0)
    scheduler.add_job(execute_create_stock_fund_industry_detail_intraday, 'cron', hour=20, minute=16, second=0)

    scheduler.add_job(execute_create_stock_fund_industry_detail_intraday, 'cron', hour=22, minute=16, second=0)

    # 资金流--行业--详细--排行
    scheduler.add_job(execute_create_stock_fund_industry_detail_rank, 'cron', hour=16, minute=43, second=0)
    scheduler.add_job(execute_create_stock_fund_industry_detail_rank, 'cron', hour=20, minute=42, second=0)
    scheduler.add_job(execute_create_stock_fund_industry_detail_rank, 'cron', hour=18, minute=43, second=0)

    scheduler.add_job(execute_create_stock_fund_industry_detail_rank, 'cron', hour=21, minute=43, second=0)

    # 资金流--概念--详细--即时
    scheduler.add_job(execute_create_stock_fund_concept_detail_intraday, 'cron', hour=16, minute=42, second=0)
    scheduler.add_job(execute_create_stock_fund_concept_detail_intraday, 'cron', hour=18, minute=42, second=0)
    scheduler.add_job(execute_create_stock_fund_concept_detail_intraday, 'cron', hour=21, minute=18, second=0)

    scheduler.add_job(execute_create_stock_fund_concept_detail_intraday, 'cron', hour=22, minute=18, second=0)

    # 资金流--概念--详细--排行
    scheduler.add_job(execute_create_stock_fund_concept_detail_rank, 'cron', hour=16, minute=24, second=0)
    scheduler.add_job(execute_create_stock_fund_concept_detail_rank, 'cron', hour=18, minute=24, second=0)
    scheduler.add_job(execute_create_stock_fund_concept_detail_rank, 'cron', hour=21, minute=23, second=0)

    scheduler.add_job(execute_create_stock_fund_concept_detail_rank, 'cron', hour=22, minute=23, second=0)

    # 股池--涨停
    scheduler.add_job(execute_create_stock_pool_zt, 'cron', hour=16, minute=35, second=0)
    scheduler.add_job(execute_create_stock_pool_zt, 'cron', hour=18, minute=35, second=0)
    scheduler.add_job(execute_create_stock_pool_zt, 'cron', hour=20, minute=37, second=0)

    scheduler.add_job(execute_create_stock_pool_zt, 'cron', hour=21, minute=37, second=0)

    # 股池--强势
    scheduler.add_job(execute_create_stock_pool_strong, 'cron', hour=16, minute=48, second=0)
    scheduler.add_job(execute_create_stock_pool_strong, 'cron', hour=18, minute=48, second=0)
    scheduler.add_job(execute_create_stock_pool_strong, 'cron', hour=20, minute=48, second=0)

    scheduler.add_job(execute_create_stock_pool_strong, 'cron', hour=21, minute=48, second=0)

    # 股池--次新
    scheduler.add_job(execute_create_stock_pool_sub_new, 'cron', hour=16, minute=55, second=0)
    scheduler.add_job(execute_create_stock_pool_sub_new, 'cron', hour=18, minute=55, second=0)
    scheduler.add_job(execute_create_stock_pool_sub_new, 'cron', hour=20, minute=55, second=0)

    scheduler.add_job(execute_create_stock_pool_sub_new, 'cron', hour=21, minute=55, second=0)

    # 股池--炸板
    scheduler.add_job(execute_create_stock_pool_zb, 'cron', hour=16, minute=23, second=0)
    scheduler.add_job(execute_create_stock_pool_zb, 'cron', hour=18, minute=23, second=0)
    scheduler.add_job(execute_create_stock_pool_zb, 'cron', hour=20, minute=23, second=0)

    scheduler.add_job(execute_create_stock_pool_zb, 'cron', hour=22, minute=23, second=0)

    # 股池--跌停
    scheduler.add_job(execute_create_stock_pool_dt, 'cron', hour=17, minute=12, second=0)
    scheduler.add_job(execute_create_stock_pool_dt, 'cron', hour=18, minute=12, second=0)
    scheduler.add_job(execute_create_stock_pool_dt, 'cron', hour=20, minute=12, second=0)

    scheduler.add_job(execute_create_stock_pool_dt, 'cron', hour=22, minute=12, second=0)

    # 龙虎榜--详情--东财
    scheduler.add_job(execute_create_stock_lhb_detail_em, 'cron', hour=18, minute=23, second=0)

    # 龙虎榜--每日活跃营业部--东财
    scheduler.add_job(execute_create_stock_lhb_hyyyb_em, 'cron', hour=18, minute=46, second=0)

    # 龙虎榜--营业部详情数据--东财
    scheduler.add_job(execute_create_stock_lhb_yyb_detail_em, 'cron', hour=19, minute=7, second=20)


    #
    # # # 当天数据检查
    # # scheduler.add_job(execute_stock_current_day_check, 'cron', hour=23, minute=20, second=0)
    # # scheduler.add_job(execute_stock_history_current_day_check, 'cron', hour=23, minute=30, second=0)

    scheduler.start()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    # add lock for scheduler start, to avoid overlap running in multi threads
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('127.0.0.1', 47200))
    except socket.error:
        log.error('scheduler already started, DO NOTHING!!!')
    else:
        init_scheduler()
        log.info('scheduler started!!!')


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


if __name__ == '__main__':
    try:
        log.info(
            """\n
 /$$$$$$$$                   /$$      /$$$$$$  /$$$$$$$  /$$$$$$
| $$_____/                  | $$     /$$__  $$| $$__  $$|_  $$_/
| $$    /$$$$$$   /$$$$$$$ /$$$$$$  | $$  | $$| $$  | $$  | $$  
| $$$$$|____  $$ /$$_____/|_  $$_/  | $$$$$$$$| $$$$$$$/  | $$  
| $$__/ /$$$$$$$|  $$$$$$   | $$    | $$__  $$| $$____/   | $$  
| $$   /$$__  $$ |____  $$  | $$ /$$| $$  | $$| $$        | $$  
| $$  |  $$$$$$$ /$$$$$$$/  |  $$$$/| $$  | $$| $$       /$$$$$$
|__/   |_______/|_______/    |___/  |__/  |__/|__/      |______/

            """
        )
        uvicorn.run(
            app=f'{Path(__file__).stem}:app',
            host=settings.UVICORN_HOST,
            port=settings.UVICORN_PORT,
            reload=settings.UVICORN_RELOAD,
        )
    except Exception as e:
        log.error(f'❌ FastAPI start failed: {e}')

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
from app.task.stock_fund_concept_intraday_task import execute_create_stock_fund_concept_intraday
from app.task.stock_fund_concept_rank_task import execute_create_stock_fund_concept_rank
from app.task.stock_fund_industry_intraday_task import execute_create_stock_fund_industry_intraday
from app.task.stock_fund_single_intraday import execute_create_stock_fund_single_intraday
from app.task.stock_fund_single_rank_task import execute_create_stock_fund_single_rank
from app.task.stock_history_hfq_task import execute_create_stock_histories_hfq_0_1000, \
    execute_create_stock_histories_hfq_1000_2000, execute_create_stock_histories_hfq_2000_3000, \
    execute_create_stock_histories_hfq_3000_4000, execute_create_stock_histories_hfq_4000_5000
from app.task.stock_history_qfq_task import execute_create_stock_histories_qfq_0_1000, \
    execute_create_stock_histories_qfq_1000_2000, execute_create_stock_histories_qfq_3000_4000, \
    execute_create_stock_histories_qfq_2000_3000, execute_create_stock_histories_qfq_4000_5000
from app.task.stock_history_task import execute_create_stock_histories_0_1000, execute_create_stock_histories_1000_2000, \
    execute_create_stock_histories_2000_3000, execute_create_stock_histories_3000_4000, \
    execute_create_stock_histories_4000_5000
from app.task.stock_news_task import execute_create_stock_news_0_1000, execute_create_stock_news_1000_2000, \
    execute_create_stock_news_2000_3000, execute_create_stock_news_3000_4000, execute_create_stock_news_4000_5000
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

app = register_app()

jobstores = {
    'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
}
scheduler = BackgroundScheduler(jobstores=jobstores)


def init_scheduler():
    #历史行情 - 不复权
    scheduler.add_job(execute_create_stock_histories_0_1000, 'cron', hour=16, minute=0, second=0)
    scheduler.add_job(execute_create_stock_histories_1000_2000, 'cron', hour=16, minute=30, second=0)
    scheduler.add_job(execute_create_stock_histories_2000_3000, 'cron', hour=17, minute=0, second=0)
    scheduler.add_job(execute_create_stock_histories_3000_4000, 'cron', hour=17, minute=30, second=0)
    scheduler.add_job(execute_create_stock_histories_4000_5000, 'cron', hour=18, minute=0, second=0)

    # 历史行情 - 前复权
    scheduler.add_job(execute_create_stock_histories_qfq_0_1000, 'cron', hour=18, minute=30, second=0)
    scheduler.add_job(execute_create_stock_histories_qfq_1000_2000, 'cron', hour=19, minute=0, second=0)
    scheduler.add_job(execute_create_stock_histories_qfq_2000_3000, 'cron', hour=19, minute=30, second=0)
    scheduler.add_job(execute_create_stock_histories_qfq_3000_4000, 'cron', hour=20, minute=0, second=0)
    scheduler.add_job(execute_create_stock_histories_qfq_4000_5000, 'cron', hour=20, minute=30, second=0)

    # 历史行情 - 后复权
    scheduler.add_job(execute_create_stock_histories_hfq_0_1000, 'cron', hour=21, minute=0, second=0)
    scheduler.add_job(execute_create_stock_histories_hfq_1000_2000, 'cron', hour=21, minute=30, second=0)
    scheduler.add_job(execute_create_stock_histories_hfq_2000_3000, 'cron', hour=22, minute=0, second=0)
    scheduler.add_job(execute_create_stock_histories_hfq_3000_4000, 'cron', hour=22, minute=30, second=0)
    scheduler.add_job(execute_create_stock_histories_hfq_4000_5000, 'cron', hour=23, minute=0, second=0)

    # 公司新闻
    scheduler.add_job(execute_create_stock_news_0_1000, 'cron', hour=16, minute=10, second=0)
    scheduler.add_job(execute_create_stock_news_1000_2000, 'cron', hour=17, minute=11, second=0)
    scheduler.add_job(execute_create_stock_news_2000_3000, 'cron', hour=18, minute=12, second=0)
    scheduler.add_job(execute_create_stock_news_3000_4000, 'cron', hour=19, minute=13, second=0)
    scheduler.add_job(execute_create_stock_news_4000_5000, 'cron', hour=20, minute=14, second=0)

    # 盘口异动
    scheduler.add_job(execute_create_stock_change_abnormal, 'cron', hour=20, minute=50, second=0)
    scheduler.add_job(execute_create_stock_change_abnormal, 'cron', hour=23, minute=40, second=0)

    # 千股千评
    scheduler.add_job(execute_create_stock_comment, 'cron', hour=19, minute=50, second=0)
    scheduler.add_job(execute_create_stock_comment, 'cron', hour=23, minute=20, second=0)

    # 公司动态
    scheduler.add_job(execute_create_stock_company_event, 'cron', hour=22, minute=10, second=0)

    # 技术指标--创新高
    scheduler.add_job(execute_create_stock_rank_cxg, 'cron', hour=17, minute=50, second=0)
    scheduler.add_job(execute_create_stock_rank_cxg, 'cron', hour=21, minute=30, second=0)

    # 技术指标--创新低
    scheduler.add_job(execute_create_stock_rank_cxd, 'cron', hour=17, minute=55, second=0)
    scheduler.add_job(execute_create_stock_rank_cxd, 'cron', hour=21, minute=40, second=0)

    # 技术指标--连续上涨
    scheduler.add_job(execute_create_stock_rank_lxsz, 'cron', hour=18, minute=40, second=0)
    scheduler.add_job(execute_create_stock_rank_lxsz, 'cron', hour=21, minute=50, second=0)

    # 技术指标--连续下跌
    scheduler.add_job(execute_create_stock_rank_lxxd, 'cron', hour=18, minute=50, second=0)
    scheduler.add_job(execute_create_stock_rank_lxxd, 'cron', hour=21, minute=50, second=0)

    # 技术指标--持续放量
    scheduler.add_job(execute_create_stock_rank_cxfl, 'cron', hour=17, minute=10, second=0)
    scheduler.add_job(execute_create_stock_rank_cxfl, 'cron', hour=22, minute=40, second=0)

    # 技术指标--持续缩量
    scheduler.add_job(execute_create_stock_rank_cxsl, 'cron', hour=17, minute=20, second=0)
    scheduler.add_job(execute_create_stock_rank_cxsl, 'cron', hour=22, minute=50, second=0)

    # 技术指标--向上突破
    scheduler.add_job(execute_create_stock_rank_xstp, 'cron', hour=18, minute=55, second=0)
    scheduler.add_job(execute_create_stock_rank_xstp, 'cron', hour=23, minute=46, second=0)

    # 技术指标--向下突破
    scheduler.add_job(execute_create_stock_rank_xxtp, 'cron', hour=18, minute=25, second=0)
    scheduler.add_job(execute_create_stock_rank_xxtp, 'cron', hour=23, minute=45, second=0)

    # 技术指标--量价齐升
    scheduler.add_job(execute_create_stock_rank_ljqs, 'cron', hour=18, minute=20, second=0)
    scheduler.add_job(execute_create_stock_rank_ljqs, 'cron', hour=23, minute=10, second=0)

    # 技术指标--量价齐跌
    scheduler.add_job(execute_create_stock_rank_ljqd, 'cron', hour=18, minute=15, second=0)
    scheduler.add_job(execute_create_stock_rank_ljqd, 'cron', hour=23, minute=11, second=0)

    # 技术指标--险资举牌
    scheduler.add_job(execute_create_stock_rank_xzjp, 'cron', hour=19, minute=45, second=0)
    scheduler.add_job(execute_create_stock_rank_xzjp, 'cron', hour=23, minute=12, second=0)

    # 资金流--个股--即时
    scheduler.add_job(execute_create_stock_fund_single_intraday, 'cron', hour=23, minute=12, second=0)

    # 资金流--个股--排行
    scheduler.add_job(execute_create_stock_fund_single_rank, 'cron', hour=23, minute=20, second=0)

    # 资金流--概念--即时
    scheduler.add_job(execute_create_stock_fund_concept_intraday, 'cron', hour=20, minute=20, second=0)

    # 资金流--概念--排行
    scheduler.add_job(execute_create_stock_fund_concept_rank, 'cron', hour=20, minute=26, second=0)

    # 资金流--行业--即时
    scheduler.add_job(execute_create_stock_fund_industry_intraday, 'cron', hour=21, minute=18, second=0)

    scheduler.start()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    init_scheduler()


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

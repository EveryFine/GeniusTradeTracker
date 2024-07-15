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

app = register_app()


jobstores = {
    'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
}
scheduler = BackgroundScheduler(jobstores=jobstores)



def init_scheduler():
    # scheduler.add_job(execute_periodic_function, 'interval', seconds=10)
    scheduler.add_job(execute_create_stock_histories_0_1000, 'cron', hour=20, minute=20, second=0)
    scheduler.add_job(execute_create_stock_histories_1000_2000, 'cron', hour=20, minute=21, second=0)
    scheduler.add_job(execute_create_stock_histories_2000_3000, 'cron', hour=20, minute=22, second=0)
    scheduler.add_job(execute_create_stock_histories_3000_4000, 'cron', hour=20, minute=23, second=0)
    scheduler.add_job(execute_create_stock_histories_4000_5000, 'cron', hour=20, minute=24, second=0)

    scheduler.add_job(execute_create_stock_histories_qfq_0_1000, 'cron', hour=21, minute=30, second=0)
    scheduler.add_job(execute_create_stock_histories_qfq_1000_2000, 'cron', hour=21, minute=31, second=0)
    scheduler.add_job(execute_create_stock_histories_qfq_2000_3000, 'cron', hour=21, minute=32, second=0)
    scheduler.add_job(execute_create_stock_histories_qfq_3000_4000, 'cron', hour=21, minute=33, second=0)
    scheduler.add_job(execute_create_stock_histories_qfq_4000_5000, 'cron', hour=21, minute=34, second=0)

    scheduler.add_job(execute_create_stock_histories_hfq_0_1000, 'cron', hour=23, minute=20, second=0)
    scheduler.add_job(execute_create_stock_histories_hfq_1000_2000, 'cron', hour=23, minute=21, second=0)
    scheduler.add_job(execute_create_stock_histories_hfq_2000_3000, 'cron', hour=23, minute=22, second=0)
    scheduler.add_job(execute_create_stock_histories_hfq_3000_4000, 'cron', hour=23, minute=23, second=0)
    scheduler.add_job(execute_create_stock_histories_hfq_4000_5000, 'cron', hour=23, minute=24, second=0)

    scheduler.add_job(execute_create_stock_news_0_1000, 'cron', hour=22, minute=10, second=0)
    scheduler.add_job(execute_create_stock_news_1000_2000, 'cron', hour=22, minute=11, second=0)
    scheduler.add_job(execute_create_stock_news_2000_3000, 'cron', hour=22, minute=12, second=0)
    scheduler.add_job(execute_create_stock_news_3000_4000, 'cron', hour=22, minute=13, second=0)
    scheduler.add_job(execute_create_stock_news_4000_5000, 'cron', hour=22, minute=14, second=0)
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

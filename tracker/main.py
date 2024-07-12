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

from datetime import datetime
from pathlib import Path

import uvicorn
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.background import BackgroundScheduler
from sqlmodel import SQLModel, Session

from app.common.log import log
from app.core.conf import settings
from app.core.db import engine
from app.core.register import register_app
from app.crud.crud_stock_history import create_part_stock_histories

app = register_app()


jobstores = {
    'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
}
scheduler = BackgroundScheduler(jobstores=jobstores)

def execute_periodic_function():
    log.info(f'定期任务执行时间：{datetime.now()}')


def execute_create_stock_histories_0_1000():
    log.info(f"{datetime.now()} schedule task [create stock histories 0-1000] start")
    with Session(engine) as session:
        stock_offset = 0
        stock_limit = 1000
        create_count = create_part_stock_histories(session=session, stock_offset=stock_offset, stock_limit=stock_limit)
        log.info(f"{datetime.now()} schedule task [create stock histories 0-1000] end, create count: {create_count}")


def execute_create_stock_histories_1000_2000():
    log.info(f"{datetime.now()} schedule task [create stock histories 1000-2000] start")
    with Session(engine) as session:
        stock_offset = 1000
        stock_limit = 1000
        create_count = create_part_stock_histories(session=session, stock_offset=stock_offset, stock_limit=stock_limit)
        log.info(f"{datetime.now()} schedule task [create stock histories 1000-2000] end, create count: {create_count}")


def execute_create_stock_histories_2000_3000():
    log.info(f"{datetime.now()} schedule task [create stock histories 2000-3000] start")
    with Session(engine) as session:
        stock_offset = 2000
        stock_limit = 1000
        create_count = create_part_stock_histories(session=session, stock_offset=stock_offset, stock_limit=stock_limit)
        log.info(f"{datetime.now()} schedule task [create stock histories 2000-3000] end, create count: {create_count}")


def execute_create_stock_histories_3000_4000():
    log.info(f"{datetime.now()} schedule task [create stock histories 3000-4000] start")
    with Session(engine) as session:
        stock_offset = 3000
        stock_limit = 1000
        create_count = create_part_stock_histories(session=session, stock_offset=stock_offset, stock_limit=stock_limit)
        log.info(f"{datetime.now()} schedule task [create stock histories 3000-4000] end, create count: {create_count}")


def execute_create_stock_histories_4000_5000():
    log.info(f"{datetime.now()} schedule task [create stock histories 4000-5000] start")
    with Session(engine) as session:
        stock_offset = 4000
        stock_limit = 1000
        create_count = create_part_stock_histories(session=session, stock_offset=stock_offset, stock_limit=stock_limit)
        log.info(f"{datetime.now()} schedule task [create stock histories 4000-5000] end, create count: {create_count}")


def init_scheduler():
    # scheduler.add_job(execute_periodic_function, 'interval', seconds=10)
    scheduler.add_job(execute_create_stock_histories_0_1000, 'cron', hour=19, minute=45, second=59)
    scheduler.add_job(execute_create_stock_histories_1000_2000, 'cron', hour=19, minute=46, second=59)
    scheduler.add_job(execute_create_stock_histories_2000_3000, 'cron', hour=19, minute=47, second=59)
    scheduler.add_job(execute_create_stock_histories_3000_4000, 'cron', hour=19, minute=48, second=59)
    scheduler.add_job(execute_create_stock_histories_4000_5000, 'cron', hour=19, minute=49, second=59)
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

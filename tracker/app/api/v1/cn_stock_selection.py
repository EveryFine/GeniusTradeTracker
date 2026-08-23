# -*- coding: utf-8 -*-
from fastapi import APIRouter

from app.api.deps import SessionDep
from app.task.mariadb_cn_stock_selection_task import execute_sync_cn_stock_selection_last_3_days

router = APIRouter()


@router.post('/sync_last_3_days', response_model=int)
def sync_last_3_days(session: SessionDep):
    """Trigger sync from MariaDB (last 3 days) to Postgres."""
    count = execute_sync_cn_stock_selection_last_3_days()
    return count

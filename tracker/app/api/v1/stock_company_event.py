# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_company_event
   Description :
   Author :       EveryFine
   Date：          2024/7/21
-------------------------------------------------
   Change Activity:
                   2024/7/21:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

from datetime import date

from fastapi import APIRouter

from app.api.deps import SessionDep
from app.crud.crud_stock_company_event import create_all_stock_company_events, create_part_stock_company_events

router = APIRouter()


@router.post("/", response_model=int)
def create_stock_company_events(session: SessionDep):
    created_count = create_all_stock_company_events(session=session)
    return created_count


@router.post("/part", response_model=int)
def create_stock_company_events_part(session: SessionDep, start_date: date = date(2013, 1, 1),
                                     end_date: date = date.today()):
    created_count = create_part_stock_company_events(session=session, start_date=start_date, end_date=end_date)
    return created_count

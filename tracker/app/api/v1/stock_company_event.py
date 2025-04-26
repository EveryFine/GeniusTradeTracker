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
from fastapi import APIRouter, HTTPException
import traceback

from app.api.deps import SessionDep
from app.crud.crud_stock_company_event import create_all_stock_company_events, create_part_stock_company_events

router = APIRouter()


@router.post("/", response_model=int)
def create_stock_company_events(session: SessionDep):
    try:
        created_count = create_all_stock_company_events(session=session)
        return created_count
    except Exception as e:
        error_msg = f"Error creating stock company events: {str(e)}\n{traceback.format_exc()}"
        raise HTTPException(status_code=500, detail=error_msg)


@router.post("/part", response_model=int)
def create_stock_company_events_part(session: SessionDep, start_date: date = date(2013, 1, 1),
                                     end_date: date = date.today()):
    try:
        created_count = create_part_stock_company_events(session=session, start_date=start_date, end_date=end_date)
        return created_count
    except Exception as e:
        error_msg = f"Error creating part stock company events: {str(e)}\n{traceback.format_exc()}"
        raise HTTPException(status_code=500, detail=error_msg)

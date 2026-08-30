# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_board_concept_em
   Description :
   Author :       EveryFine
   Date：          2025/9/7
-------------------------------------------------
   Change Activity:
                   2025/9/7:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

import traceback

from fastapi import APIRouter, HTTPException

from app.api.deps import SessionDep
from app.common.log import log
from app.crud.crud_stock_board_concept_em import create_stock_board_concept_em, get_unique_board_symbols_last_year

router = APIRouter()


@router.post("/", response_model=int)
def create_all_stock_board_concept_em(session: SessionDep):
    try:
        create_count = create_stock_board_concept_em(session=session)
        return create_count
    except Exception as e:
        error_msg = f"Error creating stock_board_concept_em: {str(e)}\n{traceback.format_exc()}"
        log.error(error_msg)
        raise HTTPException(status_code=500, detail=error_msg)


@router.get('/unique_symbols_last_year')
def unique_symbols_last_year(session: SessionDep):
    try:
        return get_unique_board_symbols_last_year(session)
    except Exception as e:
        error_msg = f"Error fetching unique symbols: {str(e)}\n{traceback.format_exc()}"
        log.error(error_msg)
        raise HTTPException(status_code=500, detail=error_msg)

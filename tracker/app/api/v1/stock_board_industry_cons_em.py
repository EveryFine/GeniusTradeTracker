# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_board_industry_cons_em
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
from app.crud.crud_stock_board_industry_cons_em import create_stock_board_industry_cons_em, create_stock_board_industry_cons_em_by_board_name

router = APIRouter()


@router.post("/", response_model=int)
def create_all_stock_board_industry_cons_em(session: SessionDep):
    try:
        create_count = create_stock_board_industry_cons_em(session=session)
        return create_count
    except Exception as e:
        error_msg = f"Error creating create_stock_board_industry_cons_em: {str(e)}\n{traceback.format_exc()}"
        log.error(error_msg)
        raise HTTPException(status_code=500, detail=error_msg)


@router.post("/by_board_name", response_model=int)
def create_stock_board_industry_cons_em_by_name(
    session: SessionDep,
    board_name: str,
):
    """按板块名称或板块代码查询对应成分股，并写入数据库。"""
    try:
        create_count = create_stock_board_industry_cons_em_by_board_name(
            session=session,
            board_name=board_name,
        )
        return create_count
    except Exception as e:
        error_msg = (
            f"Error creating stock board industry constituents by board_name "
            f"{board_name}': {str(e)}\n{traceback.format_exc()}"
        )
        log.error(error_msg)
        raise HTTPException(status_code=500, detail=error_msg)
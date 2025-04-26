# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_comment
   Description :
   Author :       EveryFine
   Date：          2024/7/18
-------------------------------------------------
   Change Activity:
                   2024/7/18:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

from fastapi import APIRouter, HTTPException
import traceback

from app.api.deps import SessionDep
from app.crud.crud_stock_comment import create_stock_comments

router = APIRouter()


@router.post("/", response_model=int)
def create_all_stock_comments(session: SessionDep):
    try:
        create_count = create_stock_comments(session=session)
        return create_count
    except Exception as e:
        error_msg = f"Error creating stock comments: {str(e)}\n{traceback.format_exc()}"
        raise HTTPException(status_code=500, detail=error_msg)


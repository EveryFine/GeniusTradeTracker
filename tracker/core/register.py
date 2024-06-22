# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     register
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

from fastapi import FastAPI

from app.router import route
from core.conf import settings


def register_app():
    # FastAPI
    app = FastAPI(
        title=settings.TITLE,
        version=settings.VERSION,
        description=settings.DESCRIPTION
    )

    register_router(app)

    return app


def register_router(app):
    """
    注册路由
    :param app: FastAPI
    :return:
    """
    app.include_router(route)

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

from app.api.routers import v1
from app.core.conf import settings
from app.middleware.access_middle import AccessMiddleware
from app.router import route


def register_app():
    # FastAPI
    app = FastAPI(
        title=settings.TITLE,
        version=settings.VERSION,
        description=settings.DESCRIPTION
    )

    register_middleware(app)

    register_router(app)

    return app


def register_router(app):
    """
    注册路由
    :param app: FastAPI
    :return:
    """
    app.include_router(route)
    app.include_router(v1)


def register_middleware(app) -> None:
    # 接口访问日志
    if settings.MIDDLEWARE_ACCESS:
        app.add_middleware(AccessMiddleware)

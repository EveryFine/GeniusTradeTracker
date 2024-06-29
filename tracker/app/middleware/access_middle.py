# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     access_middleware
   Description :
   Author :       EveryFine
   Date：          2024/6/29
-------------------------------------------------
   Change Activity:
                   2024/6/29:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

from datetime import datetime

from starlette.middleware.base import BaseHTTPMiddleware

from fastapi import Request, Response

from app.common.log import log


class AccessMiddleware(BaseHTTPMiddleware):
    """
    记录请求日志
    """

    async def dispatch(self, request: Request, call_next) -> Response:
        start_time = datetime.now()
        response = await call_next(request)
        end_time = datetime.now()
        log.info(f'{response.status_code} {request.client.host} {request.method} {request.url} {end_time - start_time}')
        return response

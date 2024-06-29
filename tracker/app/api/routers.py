# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     routers
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

from fastapi import APIRouter

from app.api.v1 import artist
from app.core.conf import settings

v1 = APIRouter(prefix=settings.API_V1_STR)

v1.include_router(artist.router, prefix='/artist', tags=['艺术家'])

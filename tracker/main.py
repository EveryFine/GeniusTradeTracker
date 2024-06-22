# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     main
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

app = FastAPI()

app.include_router(route)

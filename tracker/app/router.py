# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     router
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

from fastapi import APIRouter

route = APIRouter()


@route.get("/")
async def root():
    return {"message": "Hello World"}


@route.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

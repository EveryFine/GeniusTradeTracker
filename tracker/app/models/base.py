# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     base
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

from sqlmodel import Field

id_key = Field(exclude=True, primary_key=True, description='主键id')
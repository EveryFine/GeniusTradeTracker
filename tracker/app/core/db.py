# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     db
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

from sqlmodel import create_engine

from app.core.conf import settings

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))

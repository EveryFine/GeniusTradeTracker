# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     path_conf
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

import os
from pathlib import Path

# 获取项目根目录
# 或使用绝对路径，指到 tracker 目录为止
BasePath = Path(__file__).resolve().parent.parent.parent

# 日志文件路径
LogPath = os.path.join(BasePath, 'app', 'log')
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

import uvicorn

from app.common.log import log
from app.core.conf import settings
from app.core.register import register_app

app = register_app()

if __name__ == '__main__':
    try:
        log.info(
            """\n
 /$$$$$$$$                   /$$      /$$$$$$  /$$$$$$$  /$$$$$$
| $$_____/                  | $$     /$$__  $$| $$__  $$|_  $$_/
| $$    /$$$$$$   /$$$$$$$ /$$$$$$  | $$  | $$| $$  | $$  | $$  
| $$$$$|____  $$ /$$_____/|_  $$_/  | $$$$$$$$| $$$$$$$/  | $$  
| $$__/ /$$$$$$$|  $$$$$$   | $$    | $$__  $$| $$____/   | $$  
| $$   /$$__  $$ |____  $$  | $$ /$$| $$  | $$| $$        | $$  
| $$  |  $$$$$$$ /$$$$$$$/  |  $$$$/| $$  | $$| $$       /$$$$$$
|__/   |_______/|_______/    |___/  |__/  |__/|__/      |______/

            """
        )
        uvicorn.run(
            host=settings.UVICORN_HOST,
            port=settings.UVICORN_PORT,
            reload=settings.UVICORN_RELOAD,
        )
    except Exception as e:
        log.error(f'❌ FastAPI start failed: {e}')

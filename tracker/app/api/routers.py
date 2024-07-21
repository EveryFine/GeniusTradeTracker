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

from app.api.v1 import artist, stock_exchange, stock_info, stock_history, stock_history_qfq, stock_history_hfq, \
    stock_news, stock_trade_date, stock_change_abnormal, stock_comment, stock_company_event, stock_rank_cxg, \
    stock_rank_cxd, stock_rank_lxsz, stock_rank_lxxd, stock_rank_cxfl, stock_rank_cxsl, stock_rank_xstp
from app.core.conf import settings

v1 = APIRouter(prefix=settings.API_V1_STR)

v1.include_router(artist.router, prefix='/artist', tags=['艺术家'])

v1.include_router(stock_exchange.router, prefix='/exchange', tags=['证券交易所'])

v1.include_router(stock_info.router, prefix='/info', tags=['股票信息'])

v1.include_router(stock_history.router, prefix='/history', tags=['股票历史行情'])

v1.include_router(stock_history_qfq.router, prefix='/hqfq', tags=['股票历史行情-前复权'])

v1.include_router(stock_history_hfq.router, prefix='/hhfq', tags=['股票历史行情-后复权'])

v1.include_router(stock_news.router, prefix='/news', tags=['个股新闻'])

v1.include_router(stock_trade_date.router, prefix='/trade_date', tags=['交易日'])

v1.include_router(stock_change_abnormal.router, prefix='/abnormal', tags=['盘口异动'])

v1.include_router(stock_comment.router, prefix='/comment', tags=['千股千评'])

v1.include_router(stock_company_event.router, prefix='/event', tags=['公司动态'])

v1.include_router(stock_rank_cxg.router, prefix='/cxg', tags=['技术指标--创新高'])

v1.include_router(stock_rank_cxd.router, prefix='/cxd', tags=['技术指标--创新低'])

v1.include_router(stock_rank_lxsz.router, prefix='/lxsz', tags=['技术指标--连续上涨'])

v1.include_router(stock_rank_lxxd.router, prefix='/lxxd', tags=['技术指标--连续下跌'])

v1.include_router(stock_rank_cxfl.router, prefix='/cxfl', tags=['技术指标--持续放量'])

v1.include_router(stock_rank_cxsl.router, prefix='/cxsl', tags=['技术指标--持续缩量'])

v1.include_router(stock_rank_xstp.router, prefix='/xstp', tags=['技术指标--向上突破'])

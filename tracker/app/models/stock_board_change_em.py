# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_board_change_em
   Description :
   Author :       EveryFine
   Date：          2026/8/30
-------------------------------------------------
   Change Activity:
                   2026/8/30:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_board_change_em
   Description :    板块异动详情
                 接口：stock_board_change_em
                 目标地址：https://quote.eastmoney.com/changes/
                 描述：东方财富-行情中心-当日板块异动详情
                 限量：返回最近交易日的数据
   Author :       EveryFine
   Date：          2026/8/30
-------------------------------------------------
   Change Activity:
                   2026/8/30:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'

import datetime

from sqlmodel import SQLModel, Field


class StockBoardChangeEmBase(SQLModel):
    trade_date: datetime.date | None = Field(default=datetime.date.today(), description='日期', index=True)
    collect_time: datetime.datetime | None = Field(default_factory=lambda: datetime.datetime.now(),
                                                   description='采集时间', index=True)

    name: str | None = Field(max_length=40, description='板块名称')

    change_rate: float | None = Field(default=None, description='涨跌幅')

    main_in: float | None = Field(default=None, description='主力净流入')
    board_abnormal_count: int | None = Field(default=None, description='板块异动总次数')

    abnormal_most_stock_symbol: str | None = Field(max_length=40, description='板块异动最频繁个股及所属类型-股票代码')
    abnormal_most_stock_name: str | None = Field(max_length=40, description='板块异动最频繁个股及所属类型-股票名称')
    abnormal_most_action_type: str | None = Field(max_length=40, description='板块异动最频繁个股及所属类型-买卖方向')

    abnormal_action_type_list: str | None = Field(max_length=2000, description='板块具体异动类型列表及出现次数')

    created_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='创建时间', index=True)
    updated_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='更新时间', index=True)


class StockBoardChangeEm(StockBoardChangeEmBase, table=True):
    """stock_board_change_em表"""
    __tablename__ = "stock_board_change_em"
    id: int | None = Field(default=None, primary_key=True, description='id')


class StockBoardChangeEmCreate(StockBoardChangeEmBase):
    pass


class StockBoardChangeEmPublic(StockBoardChangeEmBase):
    id: int


class StockBoardChangeEmAllPublic(SQLModel):
    data: list[StockBoardChangeEmPublic]
    count: int

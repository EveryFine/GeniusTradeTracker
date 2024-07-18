# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     stock_comment
   Description : 千股千评数据
   Author :       EveryFine
   Date：          2024/7/18
-------------------------------------------------
   Change Activity:
                   2024/7/18:
   Product:       PyCharm
-------------------------------------------------
"""
__author__ = 'EveryFine'
import datetime

from sqlmodel import SQLModel, Field


class StockCommentBase(SQLModel):
    symbol: str = Field(max_length=20, description='股票代码', index=True)
    trade_date: datetime.date | None = Field(default=datetime.date.today(), description='交易日', index=True)
    name: str | None = Field(max_length=20, description='股票名称')
    latest_price: float | None = Field(default=None, description='最新价')
    change_rate: float | None = Field(default=None, description='涨跌幅')
    turnover_rate: float | None = Field(default=None, description='换手率')
    pe_ratio: float | None = Field(default=None, description='市盈率')
    main_cost: float | None = Field(default=None, description='主力成本')
    inst_own_pct: float | None = Field(default=None, description='机构参与度')
    overall_score: float | None = Field(default=None, description='综合得分')
    rise: int | None = Field(default=None, description='上升')
    rank: int | None = Field(default=None, description='目前排名')
    attention_index: float | None = Field(default=None, description='关注指数')
    created_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='创建时间', index=True)
    updated_at: datetime.datetime | None = Field(default=datetime.datetime.now(), description='更新时间', index=True)


class StockComment(StockCommentBase, table=True):
    """stock_comment表"""
    __tablename__ = "stock_comment"
    id: int | None = Field(default=None, primary_key=True, description='id')


class StockCommentCreate(StockCommentBase):
    pass


class StockCommentPublic(StockCommentBase):
    id: int


class StockCommentsPublic(SQLModel):
    data: list[StockCommentPublic]
    count: int

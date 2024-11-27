from typing import Optional
from sqlmodel import Field, SQLModel, ForeignKey


class Performance(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    stock_id: int | None = Field(default=None, foreign_key="stock.id")
    five_days: float
    one_month: float
    three_months: float
    year_to_date: float
    one_year: float

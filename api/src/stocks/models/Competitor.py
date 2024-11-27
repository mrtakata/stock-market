from typing import Optional
from sqlmodel import Field, SQLModel


class Competitor(SQLModel, table=False):
    id: int | None = Field(default=None, primary_key=True)
    stock_id: int | None = Field(default=None, foreign_key="stock.id")
    name: str

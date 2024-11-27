from typing import Optional
from sqlmodel import Field, SQLModel


class MarketCap(SQLModel, table=False):
    id: int | None = Field(default=None, primary_key=True)
    currency: str
    value: float

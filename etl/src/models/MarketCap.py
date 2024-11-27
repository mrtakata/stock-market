from typing import Optional
from sqlmodel import Field, SQLModel, Relationship


class MarketCap(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    stock_id: Optional[int] = Field(default=None, foreign_key="stock.id")
    stock: Optional["Stock"] = Relationship(back_populates="market_cap")
    currency: str
    value: float

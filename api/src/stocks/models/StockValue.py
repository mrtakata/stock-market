from typing import Optional
from sqlmodel import Field, SQLModel, Relationship

class StockValueBase(SQLModel):
    open: float
    high: float
    low: float
    close: float


class StockValue(StockValueBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    stock_id: Optional[int] = Field(default=None, foreign_key="stock.id")
    stock: Optional["Stock"] = Relationship(back_populates="stock_values")

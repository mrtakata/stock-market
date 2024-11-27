from datetime import datetime
from typing import Optional, List
from datetime import datetime
from sqlmodel import Field, SQLModel, Relationship
from src.models import Performance, StockValue, MarketCap


class Stock(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    status: str = Field(default="OK")
    purchased_amount: int = Field(default=0)
    purchased_status: str = Field(default="Not Purchased")
    request_data: datetime = Field(default=datetime(2024, 11, 21))
    company_code: str = Field(unique=True)
    company_name: str
    performance_data: Optional["Performance"] = Relationship(back_populates="stock")
    market_cap: Optional["MarketCap"] = Relationship(back_populates="stock")
    stock_values: Optional["StockValue"] = Relationship(back_populates="stock")
    competitors: List["Competitor"] = Relationship(back_populates="stock")

    class Config:
        arbitrary_types_allowed = True
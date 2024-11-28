from datetime import datetime
from typing import Optional, List
from datetime import datetime
from sqlmodel import Field, SQLModel, Relationship
from api.src.stocks.models.Competitor import Competitor, CompetitorBase
from api.src.stocks.models.MarketCap import MarketCap, MarketCapBase
from api.src.stocks.models.Performance import Performance, PerformanceBase
from api.src.stocks.models.StockValue import StockValue, StockValueBase


class StockBase(SQLModel):
    status: str = Field(default="OK")
    purchased_amount: int = Field(default=0)
    purchased_status: str = Field(default="Not Purchased")
    request_data: datetime = Field(default=datetime(2024, 11, 21))
    company_code: str = Field(unique=True, index=True)
    company_name: str

class Stock(StockBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    performance_data: Optional["Performance"] = Relationship(back_populates="stock")
    market_cap: Optional["MarketCap"] = Relationship(back_populates="stock")
    stock_values: Optional["StockValue"] = Relationship(back_populates="stock")
    competitors: List["Competitor"] = Relationship(back_populates="stock")

class StockWithRelations(StockBase):
    id: int
    performance_data: Optional["PerformanceBase"] = None
    market_cap: Optional["MarketCapBase"] = None
    stock_values: Optional["StockValueBase"] = None
    competitors: List["CompetitorBase"] = []
from datetime import datetime
from typing import Optional, List
from sqlmodel import Field, SQLModel,Relationship
from api.src.stocks.models import Competitor, MarketCap, Performance, StockValues

class Stock(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    status: str
    purchased_amount: int = 0
    purchased_status: str
    request_data: datetime
    company_code: str
    company_name: str
    # performance_data: Performance | None = Field(foreign_key="performance.id")
    # competitors: list["Competitor"] = Relationship(back_populates="stock")
    # stock_values: StockValues | None = Field(foreign_key="stock_values.id")
    # market_cap: MarketCap | None = Field(foreign_key="market_cap.id")
from datetime import datetime
from . import StockValue, PerformanceData, Competitor, MarketCap
from pydantic import BaseModel


class Stock(BaseModel):
    status: str
    purchased_amount: int
    purchased_status: str
    request_data: datetime
    company_code: str
    company_name: str
    stock_values: StockValue
    performance_data: PerformanceData
    competitors: list[Competitor]
    market_cap: MarketCap
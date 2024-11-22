from pydantic import BaseModel


class StockValue(BaseModel):
    open: float
    high: float
    low: float
    close: float
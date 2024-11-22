from pydantic import BaseModel


class MarketCap(BaseModel):
    currency: str
    value: float

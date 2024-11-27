from pydantic import BaseModel


class StockUpdate(BaseModel):
    amount: int
from sqlmodel import Field, SQLModel


class StockValues(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    stock_id: int | None = Field(default=None, foreign_key="stock.id")
    open: float
    high: float
    low: float
    close: float
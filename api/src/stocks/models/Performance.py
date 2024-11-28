from typing import Optional
from sqlmodel import Field, SQLModel, Relationship

class PerformanceBase(SQLModel):
    five_days: float
    one_month: float
    three_months: float
    year_to_date: float
    one_year: float

class Performance(PerformanceBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    stock_id: Optional[int] = Field(default=None, foreign_key="stock.id")
    stock: Optional["Stock"] = Relationship(back_populates="performance_data")
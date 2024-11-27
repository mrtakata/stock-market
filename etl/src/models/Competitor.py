from typing import Optional
from sqlmodel import Field, SQLModel, Relationship


class Competitor(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    stock_id: Optional[int] = Field(default=None, foreign_key="stock.id")
    stock: Optional["Stock"] = Relationship(back_populates="competitors")
    name: str

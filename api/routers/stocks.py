from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from sqlalchemy.orm import selectinload

from api.src.stocks.models import Stock, StockUpdate
from api.database import get_session

SessionDep = Annotated[Session, Depends(get_session)]

router = APIRouter(
    prefix="/stocks",
    tags=["stocks"],
    responses={404: {"description": "Not found"}},
)

@router.get("/{stock_symbol}")
async def get_stock(stock_symbol: str, session: SessionDep):
    statement = select(Stock).where(Stock.company_code == stock_symbol).options(
            selectinload(Stock.performance_data),
            selectinload(Stock.stock_values),
            selectinload(Stock.market_cap)
        )
    stock = session.exec(statement).one_or_none()
    if stock is None:
        raise HTTPException(status_code=404, detail="Stock not found")

    return stock


@router.post("/{stock_symbol}")
async def update_stock(stock_symbol: str, update_data: StockUpdate, session: SessionDep):
    statement = select(Stock).where(Stock.company_code == stock_symbol)
    stock = session.exec(statement).one_or_none()
    if stock is None:
        raise HTTPException(status_code=404, detail="Stock not found")
    

    stock.purchased_amount += update_data.amount
    stock.purchased_status = "Purchased"

    session.add(stock)
    session.commit()
    session.refresh(stock)
    return stock
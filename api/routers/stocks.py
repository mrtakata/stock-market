from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from api.src.stocks.models import *
from api.database import get_session

SessionDep = Annotated[Session, Depends(get_session)]

router = APIRouter(
    prefix="/stocks",
    tags=["stocks"],
    responses={404: {"description": "Not found"}},
)

@router.get("/{stock_symbol}")
async def get_stock(stock_symbol: str, session: SessionDep):
    # TODO: Implements connection to DB
    stock = session.exec(select(Stock).where(Stock.company_code == stock_symbol)).one()
    if stock is None:
        raise HTTPException(status_code=404, detail="Stock not found")

    return stock


@router.post("/{stock_symbol}")
async def update_stock(stock_symbol: str, update_data: StockUpdate, session: SessionDep):
    stock = session.exec(select(Stock).where(Stock.company_code == stock_symbol)).one()
    print(stock)
    stock.purchased_amount += update_data.amount
    stock.purchased_status = "Purchased"

    session.add(stock)
    session.commit()
    session.refresh(stock)
    return stock
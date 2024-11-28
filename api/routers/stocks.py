from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from api.src.stocks.models import Stock, StockUpdate, StockWithRelations
from api.database import get_session

SessionDep = Annotated[Session, Depends(get_session)]

router = APIRouter(
    prefix="/stocks",
    tags=["stocks"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{stock_symbol}", response_model=StockWithRelations)
async def get_stock(stock_symbol: str, session: SessionDep):
    statement = select(Stock).where(Stock.company_code == stock_symbol)
    stock = session.exec(statement).one_or_none()
    if stock is None:
        raise HTTPException(status_code=404, detail="Stock not found")
    print("Stock: ", stock)
    return stock


@router.post("/{stock_symbol}")
async def update_stock(stock_symbol: str, update_data: StockUpdate, session: SessionDep):
    statement = select(Stock).where(Stock.company_code == stock_symbol)
    stock = session.exec(statement).one_or_none()
    if stock is None:
        raise HTTPException(status_code=404, detail="Stock not found")
    
    if update_data.amount < 0:
        raise HTTPException(status_code=400, detail="Amount must be positive")
    
    stock.purchased_amount += update_data.amount
    stock.purchased_status = "Purchased"
    session.add(stock)
    session.commit()

    message = f"{update_data.amount} units of stock {stock_symbol} were added to your stock record"
    return {"status_code": 201, "detail": message}
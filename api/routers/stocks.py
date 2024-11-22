from fastapi import APIRouter, HTTPException
from api.src.stocks.models import *


fake_stock_db = {
    "GOOGL": {
        "company_name": "Alphabet Inc.",
        "stock_values": StockValue(open=1000.0, high=1100.0, low=990.0, close=1050.0),
        "performance_data": PerformanceData(five_days=0.05, one_month=0.1, three_months=0.2, year_to_date=0.3, one_year=0.5),
        "competitors": [Competitor(name="Microsoft"), Competitor(name="Apple Inc.")],
        "market_cap": MarketCap(currency="USD", value=2000000000000.0)
    }
}

router = APIRouter(
    prefix="/stocks",
    tags=["stocks"],
    responses={404: {"description": "Not found"}},
)

@router.get("/{stock_symbol}")
async def get_stock(stock_symbol: str):
    # TODO: Implements connection to DB
    if stock_symbol not in fake_stock_db:
        raise HTTPException(status_code=404, detail="Stock not found")
    
    stock = fake_stock_db[stock_symbol]
    return stock


@router.post("/{stock_symbol}")
async def update_stock(stock_symbol: str):
    # This is a stub, we are not actually updating the stock
    if stock_symbol not in fake_stock_db:
        raise HTTPException(status_code=404, detail="Stock not found")
    return {"message": f"Stock {stock_symbol} has been updated successfully."}
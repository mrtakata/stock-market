import json
from src.models import Stock, Performance, MarketCap, StockValue, Competitor
from src.database import create_db_and_tables, get_session
from sqlmodel import select
from datetime import datetime


DATE_FORMAT = "%Y-%m-%d"


def read_jl(path):
    data = []
    with open(path) as f:
        for line in f.readlines():
            obj = json.loads(line)
            data.append(obj)
    return data


def load_stocks(data):
    result = {"errors": 0, "inserted": 0, "not_inserted": []}
    session = get_session()

    for stock in data:
        stock_to_db = Stock(
            company_code=stock['company_code'],
            company_name=stock['company_name'],
            status=stock.get('status', 'OK'),
            purchased_amount=stock.get('purchased_amount', 0),
            purchased_status=stock.get('purchased_status', 'Not Purchased'),
            performance_data=Performance(**stock['performance']),
            market_cap=MarketCap(**stock['market_cap']),
            stock_values=StockValue(**stock['stock_values']),
            competitors=[Competitor(name=competitor) for competitor in stock.get('competitors', [])],
            request_data=datetime.strptime(stock.get('stock_values', {}).get('from', '2024-11-21'), DATE_FORMAT)
        )

        try:
            session.add(stock_to_db)
            session.commit()
            result["inserted"] += 1
        except Exception as e:
            session.rollback()
            print(e)
            print('Could not insert stock:', stock['company_code'])
            result["errors"] += 1
            result["not_inserted"].append(stock['company_code'])

    print(result)
            
    session.close()


def update_stocks(data):
    results = {"errors": 0, "updated": 0, "not_updated": []}
    session = get_session()

    for stock in data:
        statement = select(Stock).where(Stock.company_code == stock['company_code'])
        stock_to_update = session.exec(statement).one_or_none()
        if stock_to_update:
            try:
                stock_to_update.company_code=stock['company_code']
                stock_to_update.company_name=stock['company_name']
                stock_to_update.status=stock.get('status', 'OK')
                stock_to_update.purchased_amount=stock.get('purchased_amount', 0)
                stock_to_update.purchased_status=stock.get('purchased_status', 'Not Purchased')
                stock_to_update.performance_data=Performance(**stock['performance'])
                stock_to_update.market_cap=MarketCap(**stock['market_cap'])
                stock_to_update.stock_values=StockValue(**stock['stock_values'])
                stock_to_update.competitors=[Competitor(name=competitor) for competitor in stock.get('competitors', [])]
                stock_to_update.request_data=datetime.strptime(stock.get('stock_values', {}).get('from', '2024-11-21'), DATE_FORMAT)
                session.add(stock_to_update)
                session.commit()
                results["updated"] += 1
            except Exception as e:
                session.rollback()
                print(e)
                print('Could not update stock:', stock['company_code'])
                results["errors"] += 1
                results["not_updated"].append(stock['company_code'])
        else:
            print('Stock not found:', stock['company_code'])
            results["errors"] += 1
            results["not_updated"].append(stock['company_code'])
            
    session.close()
    print(results)

if __name__ == "__main__":
    data = read_jl("data/stocks.jl")
    with open("data/stocks.json", "w") as f:
        json.dump(data, f)
    create_db_and_tables()
    load_stocks(data)
    # update_stocks(data)
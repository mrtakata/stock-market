cd crawlers/stock_market
poetry run scrapy crawl market_watch -o market_watch.jl
poetry run scrapy crawl polygon -o stocks.jl
cp stocks.jl ../../etl/data/stocks.jl
cd ../../etl
poetry run python main.py

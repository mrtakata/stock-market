# STOCK-MARKET

This repo contains the code related to a challenge proposed by [CIAL D&B](https://en.cialdnb.com/). 
In this challenge, the assignment is to implement a Stocks REST API.

I've structured this project in three different subprojects:

- api, which contains the code related to the REST API implementation
- crawlers, which contains the code related to the data extraction 
- etl, which contains the code related to the data manipulation between crawlers and api

Since I used scrapy in this project, the whole ETL process could've been done using the Scrapy framework.
However, since both Market Watch's and Polygon's apis can restrict access to crawlers, I have decided to
separate both stages so I could transform data as it becomes available. With a larger infrastructure, such as
Proxies and a more event-driven architecture, the extraction process can flow better.


## Requirements

In order to run the project in this repository, you should install before:
- Python 3.10+
- [Poetry](https://pypi.org/project/poetry/)
- [Docker](https://docs.docker.com/engine/install/)

All projects were build using [Poetry](https://python-poetry.org/) as dependency manager. Each subproject has its
own `.toml` file so that one can easily verify which libraries are used in each project, and the project can be
broken down into different repositories depending on the structure chosen.


## Instalation

For each project, before running, you should go to the related folder and do:

`poetry install`

Also, a Postgres instance is needed to run the project. For this, in the root folder, you can run

`docker-compose up -d`

These environment variables were already set as example for this project, but you can change for your project.
```
  POSTGRES_USER: fastapi_admin
  POSTGRES_PASSWORD: AOsd4V9CIrLf75R9x
  POSTGRES_DB: stock_market
```

## Usage

### API

Create a `.env` file setting up `POSTGRES_URL=postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost:5432/{POSTGRES_DB}`

And, inside the folder, run: `poetry run fastapi dev main.py`

### Crawlers

Inside `crawlers/stock_market` folder, create a `.env` file, setting up `POLYGON_API_KEY` with the API_KEY given in the document.

Then, inside `crawlers/stock_market`, there are two spiders:
- market_watch: Spider to crawl data related to Performance, Market Cap, Competitors of the list of stocks to be watched. To run it: `poetry run scrapy crawl market_watch -o market_watch.jl`. It will generate a jsonlines object that will be used by `etl` for processing.
- polygon: Spider to crawl data related to Stock Values. To run it: `poetry run scrapy crawl market_watch -o market_watch.jl`. It will generate a jsonlines object that will be used by `etl` for processing.

### ETL

The ETL process is done by processing `stocks.jl` file after polygon crawler is done. To run the entire process, there is a script `extract.sh` that:
1. Runs the MarketWatch crawler;
2. Runs the Polygon crawler based on the stocks the first crawler was able to fetch;
3. Moves file to the ETL folder and process the file in `main.py`, where it uploads the data into Postgres

Run the script using `sh extract.sh` from the root of the project.

## Main Libraries

This API is built using:
- [FastAPI](https://fastapi.tiangolo.com/) as the backend. This framework makes it easy to create endpoints that can be documented with Swagger or Redocs. It also has a basic caching system.
- [sqlmodel](https://sqlmodel.tiangolo.com/) as the ORM, which is easily integrated with FastAPI, also used in the ETL process.
  
The crawlers were built using:
- [Scrapy] (https://scrapy.org/)
- [BeautifulSoup] (https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## Tasks
- Python 3.10+ ✅
- REST API should return JSON responses ✅
- The code should be available on github ✅
- The application should expose two endpoints ✅
  - [GET] to return data related to a given _stock_simbol_ ✅
  - [POST] to update the stock entity with the purchased amount based on received argument "amount" ✅
- The application should have a cache mechanism for the GET route ✅
- Data should be persisted in PostgresDB ✅
- API should be run inside a docker container, on port 8000 ✅
- The Stock model fields should be populated with the data available in [Poligon.io](https://polygon.io/docs/stocks/get_v1_open-
close__stocksticker___date) ✅
- Performance and Competitors needs to be scraped from the MarketWatch stock page using received stock symbol, available in available in the following path: https://www.marketwatch.com/investing/stock/<stock_symbol>. Ex: https://www.marketwatch.com/investing/stock/aapl ✅
- The solution should be able to update companies listed on https://www.marketwatch.com/tools/markets/stocks/country/united-states. ✅
- Create a Dockerfile that builds an image containing the ready-to-run API application. One should be able to invoke “docker run” and interact with the API
- The application should display meaningful logs for the application
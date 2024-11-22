# STOCK-MARKET

This repo contains the code related to a challenge proposed by [CIAL D&B](https://en.cialdnb.com/). 
In this challenge, the assignment is to implement a Stocks REST API.


## Instalation

Install dependencies:

`poetry init`

## Usage

For development purposes: 

`poetry run fastapi dev main.py`

## Libraries

This API is built using 
- [FastAPI](https://fastapi.tiangolo.com/) as the backend.
- [Poetry](https://python-poetry.org/) as dependency manager

## Requirements
- Python 3.10
- REST API should return JSON responses
- The code should be available on github
- The application should expose two endpoints:
  - [GET] to return data related to a given _stock_simbol_
  - [POST] to update the stock entity with the purchased amount based on received argument "amount"
- The application should have a cache mechanism for the GET route
- Data should be persisted in PostgresDB
- API should be run inside a docker container, on port 8000
- The application should display meaningful logs for the application
- The Stock model fields should be populated with the data available in [Poligon.io](https://polygon.io/docs/stocks/get_v1_open-
close__stocksticker___date)
- Performance and Competitors needs to be scraped from the MarketWatch stock page using received stock symbol, available in available in the following path: https://www.marketwatch.com/investing/stock/<stock_symbol>. Ex: https://www.marketwatch.com/investing/stock/aapl
- The solution should be able to update companies listed on https://www.marketwatch.com/tools/markets/stocks/country/united-states.


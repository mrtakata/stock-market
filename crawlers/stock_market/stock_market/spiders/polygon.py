import os
import scrapy
from dotenv import load_dotenv
import json

load_dotenv()
POLYGON_API_KEY = os.getenv("POLYGON_API_KEY")


BASE_URL = "https://api.polygon.io/v1/open-close"
STOCKS_PATH = "market_watch.jl"

class PolygonSpider(scrapy.Spider):
    name = "polygon"
    allowed_domains = ["api.polygon.io"]


    def __init__(self, date="2024-11-21", **kwargs):
        self.date = date

    def get_stocks(self):
        data = []
        with open(STOCKS_PATH, 'r') as f:
            for stock_str in f.readlines():
                stock = json.loads(stock_str)
                data.append(stock)

        return data

    def start_requests(self):
        stocks = self.get_stocks()
        for stock in stocks:
            yield scrapy.Request(
                f"{BASE_URL}/{stock['company_code']}/{self.date}",
                headers={"Authorization": f"Bearer {POLYGON_API_KEY}"},
                meta={"stock": stock},
            )


    def parse(self, response):
        stock = response.meta['stock']
        stock['stock_values'] = response.json()

        yield stock

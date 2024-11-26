import os
import scrapy
from dotenv import load_dotenv
import json

load_dotenv()
POLYGON_API_KEY = os.getenv("POLYGON_API_KEY")


BASE_URL = "https://api.polygon.io/v1/open-close"


class PolygonSpider(scrapy.Spider):
    name = "polygon"
    allowed_domains = ["api.polygon.io"]


    def __init__(self, date="2024-11-20", **kwargs):
        self.date = date
        with open("mock_data/stocks.json") as f:
            self.stocks = json.load(f)


    def start_requests(self):
        for stock in self.stocks:
            yield scrapy.Request(
                f"{BASE_URL}/{stock['symbol']}/{self.date}",
                headers={"Authorization": f"Bearer {POLYGON_API_KEY}"},
                meta={"stock": stock},
            )


    def parse(self, response):
        stock = response.meta['stock']
        stock['performance'] = response.json()

        yield stock

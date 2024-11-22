import os
import scrapy
from dotenv import load_dotenv


load_dotenv()
POLYGON_API_KEY = os.getenv("POLYGON_API_KEY")


class PolygonSpider(scrapy.Spider):
    name = "polygon"
    allowed_domains = ["api.polygon.io"]

    def start_requests(self):
        yield scrapy.Request(
            "https://api.polygon.io/v1/open-close/AAPL/2024-11-21",
            headers={"Authorization": f"Bearer {POLYGON_API_KEY}"},
        )

    def parse(self, response):
        yield response.json()

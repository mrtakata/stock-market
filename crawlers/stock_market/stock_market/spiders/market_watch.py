import os
import scrapy
from stock_market.parsers.MarketWatchListParser import MarketWatchListParser
from stock_market.parsers.MarketWatchPageParser import MarketWatchPageParser


BASE_URL = "https://www.marketwatch.com/tools/markets/stocks/country/united-states/"
TOTAL_PAGES = 103

class MarketWatchSpider(scrapy.Spider):
    name = "market_watch"
    allowed_domains = ["marketwatch.com"]
    list_parser = MarketWatchListParser()
    page_parser = MarketWatchPageParser()
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "accept-language": "pt-BR,pt;q=0.6",
        "cache-control": "max-age=0",
        "cookie": "ab_uuid=1b54fa08-5a42-48f3-9d04-e1b260f94472; letsGetMikey=enabled; fullcss-section=section-5b7e2ade8e.min.css; fullcss-error=section-5b7e2ade8e.min.css; datadome=Zq8wjrbaZeSARMB4BsgcnRIKmGj0wjjzJdcRiunOjXoGj6VMHgVkRMpf~8_hAH1_W~i8lM8kaMrVyRxmFjEpKp_VlC6KSR0pcLD6I5fg_m43oHNfyihhUZOI35GzGBIs; gdprApplies=false; refresh=off; mw_loc=%7B%22Region%22%3A%22SP%22%2C%22Country%22%3A%22BR%22%2C%22Continent%22%3A%22NA%22%2C%22ApplicablePrivacy%22%3A0%7D; recentqsmkii=Stock-US-BLEUR|Stock-US-AHFI|Stock-US-TSVT|Stock-US-AAPL|Stock-US-OONEF|Stock-US-ISBA|Stock-US-IRIX|Stock-US-MMM; usr_prof_v2=eyJpYyI6MX0%3D",
        "if-none-match": "j8jbnqi8sj7r6y",
        "priority": "u=0, i",
        "sec-ch-ua": 'Brave";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-arch": "x86",
        "sec-ch-ua-full-version-list": 'Brave";v="131.0.0.0", "Chromium";v="131.0.0.0", "Not_A Brand";v="24.0.0.0"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-model": "",
        "sec-ch-ua-platform": "Linux",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "sec-gpc": "1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",            
    }
    page_headers = {

        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "accept-language": "pt-BR,pt;q=0.8",
        "cache-control": "max-age=0",
        "cookie": "letsGetMikey=disabled; ab_uuid=1b54fa08-5a42-48f3-9d04-e1b260f94472; letsGetMikey=disabled; fullcss-section=section-5b7e2ade8e.min.css; fullcss-error=section-5b7e2ade8e.min.css; datadome=Zq8wjrbaZeSARMB4BsgcnRIKmGj0wjjzJdcRiunOjXoGj6VMHgVkRMpf~8_hAH1_W~i8lM8kaMrVyRxmFjEpKp_VlC6KSR0pcLD6I5fg_m43oHNfyihhUZOI35GzGBIs; gdprApplies=false; refresh=off; mw_loc=%7B%22Region%22%3A%22SP%22%2C%22Country%22%3A%22BR%22%2C%22Continent%22%3A%22NA%22%2C%22ApplicablePrivacy%22%3A0%7D; recentqsmkii=Stock-US-BLEUR|Stock-US-AHFI|Stock-US-TSVT|Stock-US-AAPL|Stock-US-OONEF|Stock-US-ISBA|Stock-US-IRIX|Stock-US-MMM; usr_prof_v2=eyJpYyI6MX0%3D",
        "priority": "u=0, i",
        "referer": "https://www.marketwatch.com/investing/stock/aapl",
        "sec-ch-ua": '"Brave";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-arch": "x86",
        "sec-ch-ua-full-version-list": '"Brave";v="131.0.0.0", "Chromium";v="131.0.0.0", "Not_A Brand";v="24.0.0.0"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-model": "",
        "sec-ch-ua-platform": "Linux",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "sec-gpc": "1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",

    }
    
    def start_requests(self):
        # for i in range(1, TOTAL_PAGES + 1):
        for i in range(1, 3 + 1):
            yield scrapy.Request(
                f"{BASE_URL}{i}",
                headers=self.headers,
                meta={"page": i},
            )

    def parse(self, response):
        stocks = self.list_parser.parse(response.body)
        for stock in stocks:
            headers = self.page_headers.copy()
            headers["referer"] = response.url
            yield scrapy.Request(
                stock["url"],
                headers=headers,
                meta={"stock": stock},
                callback=self.parse_stock,
            )

    def parse_stock(self, response):
        stock_data = self.page_parser.parse(response.body)

        item = {
            **response.meta['stock'],
            **stock_data
        }
        yield item

import os
import scrapy
from stock_market.parsers.MarketWatchListParser import MarketWatchListParser


BASE_URL = "https://www.marketwatch.com/tools/markets/stocks/country/united-states/"
TOTAL_PAGES = 103

class MarketWatchSpider(scrapy.Spider):
    name = "market_watch"
    allowed_domains = ["marketwatch.com"]

    def start_requests(self):
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "accept-language": "pt-BR,pt;q=0.6",
            "cache-control": "max-age=0",
            "cookie": "mw_loc=%7B%22Region%22%3A%22LR%22%2C%22Country%22%3A%22CL%22%2C%22Continent%22%3A%22NA%22%2C%22ApplicablePrivacy%22%3A0%7D; ab_uuid=1b54fa08-5a42-48f3-9d04-e1b260f94472; fullcss-home=site-6339f8c9e6.min.css; icons-loaded=true; letsGetMikey=enabled; fullcss-quote=quote-86ec49efa6.min.css; recentqsmkii=Stock-US-OONEF; fullcss-section=section-5b7e2ade8e.min.css; fullcss-error=section-5b7e2ade8e.min.css; datadome=Zq8wjrbaZeSARMB4BsgcnRIKmGj0wjjzJdcRiunOjXoGj6VMHgVkRMpf~8_hAH1_W~i8lM8kaMrVyRxmFjEpKp_VlC6KSR0pcLD6I5fg_m43oHNfyihhUZOI35GzGBIs; usr_prof_v2=eyJpYyI6MX0%3D; gdprApplies=false",
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
        for i in range(1, TOTAL_PAGES + 1):
            yield scrapy.Request(
                f"{BASE_URL}{i}",
                headers=headers,
                meta={"page": i},
            )

    def parse(self, response):
        stocks = MarketWatchListParser.parse_page(response.body)
        item = {
            "stocks": stocks,
            "page": response.meta["page"],
        }
        yield item

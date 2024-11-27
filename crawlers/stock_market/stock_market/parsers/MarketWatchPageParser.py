from bs4 import BeautifulSoup
import re

SYMBOL_NUMBER_MAP = {
    "K": 1000,
    "M": 1000000,
    "B": 1000000000,
    "T": 1000000000000
}


class MarketWatchPageParser:


    def parse(self, page):
        soup = BeautifulSoup(page, "html.parser")
        competitors = self.get_competitors(soup)
        performance = self.get_performance(soup)
        market_cap = self.get_market_cap(soup)
        data = {
            "competitors": competitors,
            "performance": performance,
            "market_cap": market_cap,
        }
        return data

    def get_performance(self, soup):
        text_to_field_map = {
            "5 Day": "five_days",
            "1 Month": "one_month",
            "3 Month": "three_months",
            "YTD": "year_to_date",
            "1 Year": "one_year",
        }
        performance = {
            "five_days": 0.0,
            "one_month": 0.0,
            "three_months": 0.0,
            "year_to_date": 0.0,
            "one_year": 0.0,
        }
        performance_tag = soup.find('div', class_="performance")
        if performance_tag is None:
            return performance
        
        table_body = performance_tag.find('tbody')
        rows = table_body.find_all('tr')

        for row in rows:
            cells = row.find_all('td')
            key = cells[0].text.strip()
            value = cells[1].find('li').text.strip().replace('%', '').replace(',', '')
            value = float(value)
            field_name = text_to_field_map[key]
            performance[field_name] = value
        return performance


    def get_competitors(self, soup):
        competitors = []
        competitors_tag = soup.find('div', class_="Competitors")
        if competitors_tag is None:
            return competitors
        
        table_body = competitors_tag.find('tbody')
        rows = table_body.find_all('tr')
        
        for row in rows:
            competitor_name = row.find('td').text.strip()
            competitors.append(competitor_name)

        return competitors
    

    def get_market_cap(self, soup):
        market_cap = {
            "currency": "",
            "value": 0.0
        }
        try:
            market_cap_tag = soup.find(string=re.compile("Market Cap", re.I)).find_next('span')

            market_cap_text = market_cap_tag.text.strip()
            currency = market_cap_text[0]
            value = market_cap_text[1:-1]
            value = value.replace(',', '')
            value_symbol = market_cap_text[-1]
            value = float(value) * SYMBOL_NUMBER_MAP[value_symbol]
            market_cap = {
                "currency": currency,
                "value": value
            }
        except Exception as e:
            print(e)
            return None

        return market_cap
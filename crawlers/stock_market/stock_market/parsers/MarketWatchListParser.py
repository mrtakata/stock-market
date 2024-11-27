from bs4 import BeautifulSoup

BASE_URL = "https://www.marketwatch.com/investing/Stock/"


class MarketWatchListParser:

    def parse(self, page):
        soup = BeautifulSoup(page, "html.parser")
        table = soup.find('table', class_="table table-condensed")
        rows = table.find_all('tr')[1:]  # Skip header

        stocks = []
        for row in rows:
            # columns: Name (with url) | Symbol | Sector|
            cells = row.find_all('td')
            url = cells[0].find('a')['href']
            full_name = cells[0].text.strip()
            full_name_split = full_name.split("(")
            company_name = full_name_split[0].strip()
            company_code = url.replace(BASE_URL, "").replace("?countryCode=US", "")
            exchange = cells[1].text.strip()
            sector = cells[2].text.strip()
            stock = {
                "company_name": company_name,
                "url": url,
                "company_code": company_code,
                "exchange": exchange,
                "sector": sector,
            }
            stocks.append(stock)
            
        return stocks


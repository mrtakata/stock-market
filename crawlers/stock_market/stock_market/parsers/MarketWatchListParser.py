from bs4 import BeautifulSoup


class MarketWatchListParser:

    @staticmethod
    def parse_page(page):
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
            name = full_name_split[0].strip()
            symbol = full_name_split[1].replace(")", "")
            exchange = cells[1].text.strip()
            sector = cells[2].text.strip()
            stock = {
                "name": name,
                "url": url,
                "symbol": symbol,
                "exchange": exchange,
                "sector": sector,
            }
            stocks.append(stock)
            
        return stocks


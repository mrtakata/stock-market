from bs4 import BeautifulSoup


class MarketWatchPageParser:


    def parse(self, page):
        soup = BeautifulSoup(page, "html.parser")
        competitors = self.get_competitors(soup)
        performance = self.get_performance(soup)
        data = {
            "competitors": competitors,
            "performance": performance
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

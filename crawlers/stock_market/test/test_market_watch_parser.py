import pytest
from stock_market.parsers.MarketWatchListParser import MarketWatchListParser

@pytest.mark.parametrize("page, expected", [
    ("""
    <table class="table table-condensed">
        <thead>
            <tr>
                <th>Name</th>
                <th>Symbol</th>
                <th>Sector</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><a href="https://www.marketwatch.com/investing/stock/aapl">Apple Inc.</a></td>
                <td>AAPL</td>
                <td>Technology</td>
            </tr>
            <tr>
                <td><a href="https://www.marketwatch.com/investing/stock/msft">Microsoft Corp.</a></td>
                <td>MSFT</td>
                <td>Technology</td>
            </tr>
        </tbody>
    </table>
    """, [
        {
            "name": "Apple Inc.",
            "url": "https://www.marketwatch.com/investing/stock/aapl",
            "symbol": "AAPL",
            "sector": "Technology",
        },
        {
            "name": "Microsoft Corp.",
            "url": "https://www.marketwatch.com/investing/stock/msft",
            "symbol": "MSFT",
            "sector": "Technology",
        },
    ])
])
def test_parse_page(page, expected):
    stocks = MarketWatchListParser.parse_page(page)
    assert stocks == expected
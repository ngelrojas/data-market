"""
    _indicator_key:
    - yield: dividend yield
    - earning_per_share_diluted : earning per share diluted
    - dividend per share = cotacao atual / dividend yield ttm (12 months)
"""

from .guru.stock_list_in_exchange import StockListInExchange
from .guru.stock_data import StockData


def get_list_exchange(symbol):
    _stock_list_in_exchange = StockListInExchange()
    return _stock_list_in_exchange.get_list_exchange(symbol)


def get_dividend_per_share(symbol, indicator_key, _type):
    _stock_data = StockData()
    return _stock_data.get_stock_indicator_data(symbol, indicator_key, _type)


_symbol = "PETR4"
_indicator_key = "yield"
_type = "a"

get_dividend_per_share(_symbol, _indicator_key, _type)

get_list_exchange(_symbol)

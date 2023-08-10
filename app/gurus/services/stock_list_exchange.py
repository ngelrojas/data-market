import requests
from ..config.base_url import API_PUBLIC_URL
from ..tools.tool import get_data_mock

# 79773


def get_list_exchange():
    try:
        _file_json = "stock_list_exchange.json"
        data = get_data_mock(_file_json)
        result = list(map(lambda x: {"company": x["company"]}, data))
        return result
    except Exception as e:
        return {"error": e}


def get_dividend_yield():
    """
    TODO: create a function interval 10 years, and to replace the '2013-0-01'
    """
    _file_json = "stock_dividend_yield.json"
    data = get_data_mock(_file_json)

    for index in range(len(data)):
        if data[index][0] >= '2013-01-01':
            data = data[index:]
            break

    return data


class StockListInExchange:

    def __init__(self):
        self.url = API_PUBLIC_URL

    def get_stock_list_in_exchange(self, symbol):
        try:
            stocks_list = f"{self.url}/exchange_stocks/{symbol}"
            response = requests.get(stocks_list)
            return response.json()
        except Exception as e:
            return {"error": e}

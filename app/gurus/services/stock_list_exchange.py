import json
from os import path
import requests
from ..config.base_url import API_PUBLIC_URL

# 79773
def get_list_exchange():
    try:
        real_path = path.realpath("gurus/mocks/stock_list_exchange.json")
        with open(real_path, "r") as data_file:
            data = json.load(data_file)
        result = list(map(lambda x: {"company": x["company"]}, data))
        return result
    except Exception as e:
        return {"error": e}


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

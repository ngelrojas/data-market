import requests
import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class StocksGuru:

    def __init__(self):
        self.api_key = os.environ.get("API_KEY")
        self.url = "https://www.alphavantage.co/query?"
        self.params = {
            "function": "TIME_SERIES_DAILY_ADJUSTED",
            "symbol": "IBM",
            "outputsize": "compact",
            "datatype": "json",
            "apikey": self.api_key,
        }

    def get_stock(self, symbol):
        try:
            self.params["symbol"] = symbol
            response = requests.get(self.url, params=self.params)
            return response.json()
        except Exception as e:
            return {"error": e}

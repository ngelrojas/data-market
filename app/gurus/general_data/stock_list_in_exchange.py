import requests
from ..config.base_url import API_PUBLIC_URL


class StockListInExchange:

    def __init__(self):
        self.url = API_PUBLIC_URL

    def get_list_exchange(self, symbol):
        try:
            data = f"BSP:{symbol}"
            url_complete = f"{self.url}/exchange_stocks/{data}"
            response = requests.get(url_complete)
            return response.json()
        except Exception as e:
            return {"error": e}


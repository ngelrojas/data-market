import requests
from ..config.base_guru import API_PUBLIC_URL


class StockData:
    def __init__(self):
        self.url = API_PUBLIC_URL

    def get_stock_indicator_data(self, symbol, indicator_key, _type):
        try:
            data = f"BSP:{symbol}"
            url_complete = f"{self.url}/stock/{data}/{indicator_key}?type={_type}"
            response = requests.get(url_complete)
            return response.json()
        except Exception as e:
            return {"error": e}

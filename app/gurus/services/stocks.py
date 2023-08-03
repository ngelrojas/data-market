import requests
from ..config.base_url import API_PUBLIC_URL


#TODO: creating for each service stock data from gurusfocus API
class StocksGuruService:

    def __init__(self):
        self.url = API_PUBLIC_URL

    def get_stock_summary(self, symbol):
        try:
            url_summary = f"{self.url}/stock/{symbol}/summary"
            response = requests.get(url_summary)
            return response.json()
        except Exception as e:
            return {"error": e}

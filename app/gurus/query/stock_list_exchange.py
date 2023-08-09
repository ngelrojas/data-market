from core.stock_list import StockList


class StockListQuery:

    def save_stock_exchange_list(self, company, exchange_name):
        stock_list = StockList.objects.create(
            company=company,
            exchange_name=exchange_name
        )
        return stock_list

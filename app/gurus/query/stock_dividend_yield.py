from core.stock_dividend_yield import StockDividendYield


class StockDividendYieldQuery:

    def save_stock_dividend_yield(self, company, exchange_name, date_indicator, dividend_yield):
        stock_dividend_yield = StockDividendYield.objects.create(
            company=company,
            exchange_name=exchange_name,
            date_indicator=date_indicator,
            dividend_yield=dividend_yield
        )
        return stock_dividend_yield
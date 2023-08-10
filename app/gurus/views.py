from rest_framework import viewsets, status
from rest_framework.response import Response
from core.market import Market
from .services.stock_list_exchange import get_list_exchange, get_dividend_yield
from .query.stock_list_exchange import StockListQuery
from .query.stock_dividend_yield import StockDividendYieldQuery


class StocksView(viewsets.ModelViewSet):
    serializer_class = ''
    queryset = Market.objects.all()

    def list(self, request, *args, **kwargs):
        symbol = request.GET.get('symbol')
        _stock_list_query = StockListQuery()
        _stock_dividend_yield_query = StockDividendYieldQuery()
        # _stock_list_exchange = get_list_exchange()
        _stock_list_exchange = get_dividend_yield()
        for index in range(len(_stock_list_exchange)):
            _stock_dividend_yield_query.save_stock_dividend_yield("", symbol, _stock_list_exchange[index][0], _stock_list_exchange[index][1])
            # print("date", _stock_list_exchange[index][0])
            # print("yield", _stock_list_exchange[index][1])

        # for stock in _stock_list_exchange:
        #     _stock_list_query.save_stock_exchange_list(stock.get("company"), symbol)

        return Response({
            'data': _stock_list_exchange
        }, status=status.HTTP_200_OK)
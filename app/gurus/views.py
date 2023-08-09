from rest_framework import viewsets, status
from rest_framework.response import Response
from core.market import Market
from .services.stock_list_exchange import get_list_exchange
from .query.stock_list_exchange import StockListQuery


class StocksView(viewsets.ModelViewSet):
    serializer_class = ''
    queryset = Market.objects.all()

    def list(self, request, *args, **kwargs):
        symbol = request.GET.get('symbol')
        _stock_list_query = StockListQuery()
        _stock_list_exchange = get_list_exchange()
        for stock in _stock_list_exchange:
            _stock_list_query.save_stock_exchange_list(stock.get("company"), symbol)

        return Response({
            'data': _stock_list_exchange
        }, status=status.HTTP_200_OK)
from rest_framework import viewsets, status
from rest_framework.response import Response
from core.market import Market
from .services.stocks import StocksGuruService
from .services.stock_list_exchange import get_list_exchange


class StocksView(viewsets.ModelViewSet):
    serializer_class = ''
    queryset = Market.objects.all()

    def list(self, request, *args, **kwargs):
        """
        TODO: the function is recovery a company list from mock data
        now we need to save in data base and create a new endpoint to get the data,
        the next step is test from real guru focus api

        """
        symbol = request.GET.get('symbol')

        _stock_list_exchange = get_list_exchange()

        return Response({
            'data': _stock_list_exchange
        }, status=status.HTTP_200_OK)
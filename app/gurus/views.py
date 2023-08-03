from rest_framework import viewsets, status
from rest_framework.response import Response
from core.market import Market
from .services.stocks import StocksGuruService


class StocksView(viewsets.ModelViewSet):
    serializer_class = ''
    queryset = Market.objects.all()

    def list(self, request, *args, **kwargs):
        symbol = request.GET.get('symbol')
        _stock_summary = StocksGuruService().get_stock_summary(symbol)
        return Response({
            'data': _stock_summary
        }, status=status.HTTP_200_OK)
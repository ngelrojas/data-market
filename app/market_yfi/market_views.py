from rest_framework import viewsets, status
from rest_framework.response import Response
from core.market import Market
from .serializers import MarketSerializer


class MarketView(viewsets.ModelViewSet):

    serializer_class = MarketSerializer
    queryset = Market.objects.all()

    def list(self, request):
        _start_date = request.GET.get('start_date')
        _end_date = request.GET.get('end_date')
        # _open = request.GET.get('open')
        # _high = request.GET.get('high')
        # _low = request.GET.get('low')
        # _close = request.GET.get('close')
        # _volume = request.GET.get('volume')
        # _dividends = request.GET.get('dividends')
        # _stock_splits = request.GET.get('stock_splits')

        if not _start_date or not _end_date:
            return Response({"error": "start_date and end_date are required"}, status=status.HTTP_400_BAD_REQUEST)

        _serializer = Market.objects.filter(date__range=(_start_date, _end_date))

        response = self.serializer_class(_serializer, many=True)

        return Response({"data": response.data}, status=status.HTTP_200_OK)

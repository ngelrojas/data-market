from rest_framework import viewsets, status
from rest_framework.response import Response
from core.market import Market
from .serializers import MarketSerializer
from .tools import DateRequired


class MarketView(viewsets.ModelViewSet):

    serializer_class = MarketSerializer
    queryset = Market.objects.all()

    def list(self, request):
        try:

            data_req = {
                "start_date": request.data.get('start_date'),
                "end_date": request.data.get('end_date'),
                "open": request.data.get('open'),
                "high": request.data.get('high'),
                "low": request.data.get('low'),
                "close": request.data.get('close'),
                "volume": request.data.get('volume'),
                "dividends": request.data.get('dividends'),
                "stock_splits": request.data.get('stock_splits')
            }
            
            # TODO: Refactor this code
            if data_req.get('start_date') or data_req.get('end_date'):
                DateRequired.dates_required(data_req.get('start_date'), data_req.get('end_date'))
            elif data_req.get('open'):
                _serializer = Market.objects.filter(open=data_req.get('open'))
            if not data_req.get('start_date') or not data_req.get('end_date'):
                return Response(
                    {"error": "start_date and end_date are required"},
                    status=status.HTTP_400_BAD_REQUEST
                )



            _serializer = Market.objects.filter(
                date__range=(data_req.get('start_date'), data_req.get('end_date'))
            )

            response = self.serializer_class(_serializer, many=True)

            return Response({"data": response.data}, status=status.HTTP_200_OK)
        except Exception as err:
            return Response(
                {"error": err},
                status=status.HTTP_400_BAD_REQUEST
            )

from core.market import Market
from rest_framework import viewsets, status
from rest_framework.response import Response

from .quotation.finance import Finance
from .quotation.save import SaveQuery


class FinanceYFIR(viewsets.ModelViewSet):
    serializer_class = ""
    queryset = Market.objects.all()

    def list(self, request):
        symbol = request.GET.get("symbol")
        start_date = request.GET.get("start_date")
        end_date = request.GET.get("end_date")
        _finance = Finance(symbol, start_date, end_date)
        _response = _finance.get_quotation_yfi()
        self.retrieve_data_market(self, symbol)

        return Response(
            {
                "data": _response,
            },
            status=status.HTTP_200_OK,
        )

    @staticmethod
    def retrieve_data_market(self, symbol):
        _ext_data = SaveQuery()
        _ext_data.saving_quotation(symbol)
        return True

from core.market import Market
from rest_framework import viewsets, status
from rest_framework.response import Response

from .extract_data_yfi import ExtractDataYFI
from .save_market_yfi import MarketYFIQuery

from tools.generate_date import get_date_ten_years_ago


class MarketYFIR(viewsets.ModelViewSet):
    serializer_class = ""
    queryset = Market.objects.all()

    def list(self, request):
        symbol = request.GET.get("symbol")
        start_date = request.GET.get("start_date")
        end_date = request.GET.get("end_date")
        data_req = {"symbol": symbol, "start_date": start_date, "end_date": end_date}
        # self.retrieve_data_market(data_req)
        # self.save_data()
        print(get_date_ten_years_ago())
        return Response(
            {
                "data": data_req,
            },
            status=status.HTTP_200_OK,
        )

    @staticmethod
    def retrieve_data_market(data_req):
        _ext_data = ExtractDataYFI()
        _ext_data.data_file_name_yfi(data_req)
        return True

    @staticmethod
    def save_data():
        _data_market = MarketYFIQuery()
        _data_market.saving_market_yfi()
        return True

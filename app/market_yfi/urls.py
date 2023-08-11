from django.urls import path
from .views import MarketYFIR
from .market_views import MarketView
from .views_finances import FinanceYFIR

app_name = 'market_yfi_recovery'

urlpatterns = [
    path('recovery', MarketYFIR.as_view({"get": "list"}),
         name='recovery'),
    path('market', MarketView.as_view({"get": "list"}), name='market'),
    path('quotation', FinanceYFIR.as_view({"get": "list"}), name='quotation'),
]
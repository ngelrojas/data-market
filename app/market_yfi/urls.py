from django.urls import path
from .views import MarketYFIR
from .market_views import MarketView

app_name = 'market_yfi_recovery'

urlpatterns = [
    path('recovery', MarketYFIR.as_view({"get": "list"}),
         name='recovery'),
    path('market', MarketView.as_view({"get": "list"}),
         name='market'),
]
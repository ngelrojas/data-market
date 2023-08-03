from django.urls import path
from .views import StocksView

app_name = 'gurus'

urlpatterns = [
    path('stocks', StocksView.as_view({"get": "list"}), name='stocks'),
]

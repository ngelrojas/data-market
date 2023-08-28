from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import MarketYFIR
from .market_views import MarketView
from .views_finances import FinanceYFIR
from graphene_django.views import GraphQLView
from .graphql.schema import schema

app_name = "market_yfi_recovery"

urlpatterns = [
    path("recovery", MarketYFIR.as_view({"get": "list"}), name="recovery"),
    path("market", MarketView.as_view({"get": "list"}), name="market"),
    path("quotation", FinanceYFIR.as_view({"get": "list"}), name="quotation"),
    path(
        "graphql/cotacoes",
        csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema)),
    ),
]

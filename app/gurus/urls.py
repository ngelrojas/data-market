from django.urls import path
from .views import StocksView
from graphene_django.views import GraphQLView

app_name = "gurus"

urlpatterns = [
    path("stocks", StocksView.as_view({"get": "list"}), name="stocks"),
    path("graphql/dividend-yield", GraphQLView.as_view(graphiql=True)),
]

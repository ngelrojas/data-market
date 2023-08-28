from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from graph.schema import schema
from gurus.graphql.schema import schema as dividends_schema
from market_yfi.graphql.schema import schema as cotacao_schema


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include("market_yfi.urls")),
    path("api/", include("gurus.urls")),
    path(
        "graphql/market", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))
    ),
    path(
        "graphql/dividend-yield",
        csrf_exempt(GraphQLView.as_view(graphiql=True, schema=dividends_schema)),
    ),
    path(
        "graphql/cotacoes",
        csrf_exempt(GraphQLView.as_view(graphiql=True, schema=cotacao_schema)),
    ),
]

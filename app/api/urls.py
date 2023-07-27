from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from graph.schema import schema

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include("market_yfi.urls")),
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]

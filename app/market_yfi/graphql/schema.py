import graphene
from graphene_django import DjangoObjectType

from core.models import Market


class MarketType(DjangoObjectType):
    class Meta:
        model = Market
        fields = (
            "id",
            "date",
            "open",
            "high",
            "low",
            "name",
            "close",
            "volume",
            "dividends",
            "stock_splits",
        )


class Query(graphene.ObjectType):
    quotations = graphene.List(MarketType)
    cotacoes = graphene.List(
        MarketType,
        start_date=graphene.Date(required=True),
        end_date=graphene.Date(required=True),
        open=graphene.Float(),
        high=graphene.Float(),
        low=graphene.Float(),
        close=graphene.Float(),
        volume=graphene.Int(),
        dividends=graphene.Float(),
        stock_splits=graphene.Float(),
        name=graphene.String(),
        first=graphene.Int(),
        pages=graphene.Int(),
    )

    def resolve_quotations(self, info, first=None, pages=None, **kwargs):
        queryset = Market.objects.all()
        if pages:
            queryset = queryset[pages:]
        if first:
            queryset = queryset[:first]
        return queryset

    def resolve_cotacoes(
        self,
        info,
        start_date,
        end_date,
        low=None,
        high=None,
        name=None,
        open=None,
        close=None,
        volume=None,
        dividends=None,
        stock_splits=None,
        first=None,
        pages=None,
    ):
        query_params = {"date__range": [start_date, end_date]}

        if open is not None:
            query_params["open__gte"] = open

        if low is not None:
            query_params["low__gte"] = low

        if high is not None:
            query_params["high__lte"] = high

        if close is not None:
            query_params["close__gte"] = close

        if volume is not None:
            query_params["volume__gte"] = volume

        if dividends is not None:
            query_params["dividends__gte"] = dividends

        if stock_splits is not None:
            query_params["stock_splits__gte"] = stock_splits

        if name is not None:
            query_params["name"] = name

        queryset = Market.objects.filter(**query_params)

        if pages:
            queryset = queryset[pages:]
        if first:
            queryset = queryset[:first]
        return queryset


schema = graphene.Schema(query=Query)

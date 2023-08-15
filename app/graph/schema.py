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
    markets = graphene.List(MarketType)
    market_between_dates = graphene.List(
        MarketType,
        start_date=graphene.Date(required=True),
        end_date=graphene.Date(required=True),
        low=graphene.Float(),
        name=graphene.String(),
        high=graphene.Float(),
        first=graphene.Int(),
        pages=graphene.Int(),
    )

    def resolve_markets(self, info, first=None, pages=None, **kwargs):
        queryset = Market.objects.all()
        if pages:
            queryset = queryset[pages:]
        if first:
            queryset = queryset[:first]
        return queryset

    def resolve_market_between_dates(
        self,
        info,
        start_date,
        end_date,
        low=None,
        high=None,
        name=None,
        first=None,
        pages=None,
    ):
        query_params = {"date__range": [start_date, end_date]}

        if low is not None:
            query_params["low__gte"] = low

        if high is not None:
            query_params["high__lte"] = high

        if name is not None:
            query_params["name"] = name

        queryset = Market.objects.filter(**query_params)

        if pages:
            queryset = queryset[pages:]
        if first:
            queryset = queryset[:first]
        return queryset


schema = graphene.Schema(query=Query)

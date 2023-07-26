import graphene
from graphene_django import DjangoObjectType

from core.models import Market


class MarketType(DjangoObjectType):
    class Meta:
        model = Market
        fields = ("date", "open", "high", "low", "close", "volume", "dividends", "stock_splits")


class Query(graphene.ObjectType):
    markets = graphene.List(MarketType)
    market_between_dates = graphene.List(
        MarketType,
        start_date=graphene.Date(required=True),
        end_date=graphene.Date(required=True),
        low=graphene.Float(),
        high=graphene.Float(),
        first=graphene.Int(),
        page=graphene.Int(),
    )

    def resolve_markets(self, info, first=None, page=None, **kwargs):
        queryset = Market.objects.all()
        if page:
            queryset = queryset[page:]
        if first:
            queryset = queryset[:first]
        return queryset

    def resolve_market_between_dates(
            self, info, start_date, end_date, low=None, high=None, first=None, page=None
    ):
        query_params = {
            'date__range': [start_date, end_date]
        }

        if low is not None:
            query_params['low__gte'] = low

        if high is not None:
            query_params['high__lte'] = high

        queryset = Market.objects.filter(**query_params)

        if page:
            queryset = queryset[page:]
        if first:
            queryset = queryset[:first]
        return queryset


schema = graphene.Schema(query=Query)

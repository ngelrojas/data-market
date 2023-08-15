import graphene
from graphene_django import DjangoObjectType

from core.stock_dividend_yield import StockDividendYield


class StockDividendYieldType(DjangoObjectType):
    class Meta:
        model = StockDividendYield
        fields = (
            "id",
            "company",
            "exchange_name",
            "date_indicator",
            "dividend_yield",
        )


class Query(graphene.ObjectType):
    stock_dividend_yields = graphene.List(StockDividendYieldType)
    stock_dividend_yield_bd = graphene.List(
        StockDividendYieldType,
        start_date=graphene.Date(required=True),
        end_date=graphene.Date(required=True),
        dividend_yield=graphene.Float(),
        company=graphene.String(),
        exchange_name=graphene.String(),
        first=graphene.Int(),
        pages=graphene.Int(),
    )

    def resolve_stock_dividend_yields(self, info, first=None, pages=None, **kwargs):
        queryset = StockDividendYield.objects.all()
        if pages:
            queryset = queryset[pages:]
        if first:
            queryset = queryset[:first]
        return queryset

    def resolve_stock_dividend_yield_bd(
        self,
        info,
        start_date,
        end_date,
        dividend_yield=None,
        company=None,
        exchange_name=None,
        first=None,
        pages=None,
    ):
        query_params = {"date_indicator__range": [start_date, end_date]}

        if dividend_yield is not None:
            query_params["dividend_yield__gte"] = dividend_yield
        if company is not None:
            query_params["company__icontains"] = company
        if exchange_name is not None:
            query_params["exchange_name__icontains"] = exchange_name

        queryset = StockDividendYield.objects.filter(**query_params)
        if pages:
            queryset = queryset[pages:]
        if first:
            queryset = queryset[:first]
        return queryset


schema = graphene.Schema(query=Query)

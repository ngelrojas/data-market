from django.utils import timezone
from rest_framework import serializers
from core.market import Market


class MarketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Market
        fields = ('date', 'open', 'high', 'low', 'close', 'volume', 'dividends', 'stock_splits', 'name')

    def get_date(self, obj):
        return timezone.now()

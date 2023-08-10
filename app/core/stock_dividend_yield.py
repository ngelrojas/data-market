from django.db import models


class StockDividendYield(models.Model):
    company = models.CharField(max_length=150, blank=True)
    exchange_name = models.CharField(max_length=150, blank=True)
    date_indicator = models.DateTimeField(null=True)
    dividend_yield = models.DecimalField(max_digits=18, decimal_places=14, null=True)

    def __str__(self):
        return self.company

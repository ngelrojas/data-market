from django.db import models


class Market(models.Model):
    date = models.DateTimeField(null=True)
    open = models.DecimalField(max_digits=18, decimal_places=14, null=True)
    high = models.DecimalField(max_digits=18, decimal_places=2, null=True)
    low = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    close = models.DecimalField(max_digits=18, decimal_places=14, null=True)
    volume = models.IntegerField(null=True)
    dividends = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    stock_splits = models.DecimalField(max_digits=12, decimal_places=2, null=True)

    def __str__(self):
        return self.id

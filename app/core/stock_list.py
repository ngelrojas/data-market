from django.db import models


class StockList(models.Model):
    company = models.CharField(max_length=150, blank=True)
    exchange_name = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.company

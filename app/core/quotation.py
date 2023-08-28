from django.db import models
from .base_stock import BaseStock


class Quotation(BaseStock):
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

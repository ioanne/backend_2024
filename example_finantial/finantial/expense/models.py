from django.db import models

from datetime import datetime


class Expense(models.Model):
    name = models.CharField(max_length=100)
    product = models.ForeignKey(
        "product.Product", on_delete=models.CASCADE, null=True, blank=True
    )
    service = models.ForeignKey(
        "service.Service", on_delete=models.CASCADE, null=True, blank=True
    )
    description = models.TextField()
    date = models.DateField(default=datetime.now)

    def __str__(self):
        return self.name

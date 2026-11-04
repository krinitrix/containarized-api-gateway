from django.db import models


class InventoryItem(models.Model):
    name = models.CharField(max_length=150)

    sku = models.CharField(
        max_length=50,
        unique=True
    )

    quantity = models.PositiveIntegerField(default=0)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.sku})"
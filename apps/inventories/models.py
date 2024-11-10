from django.db import models

from apps.products.models import Product


class InventoryLog(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="inventory_logs"
    )
    change = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.change} units - {self.product.name} on {self.date}"

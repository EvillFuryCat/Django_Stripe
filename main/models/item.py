from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    description = models.TextField(blank=True,)
    price = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name

    def display_price(self) -> int:
        return self.price

from django.conf import settings
from django.db import models


class Order(models.Model):
    "Generated Model"
    customer = models.ForeignKey(
        "authentication.Customer",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="order_customer",
    )
    restaurant = models.ForeignKey(
        "restaurants.Restaurant",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="order_restaurant",
    )
    items = models.JSONField()
    special_requests = models.TextField(
        null=True,
        blank=True,
    )
    status = models.CharField(
        max_length=50,
    )
    scheduled_time = models.DateTimeField(
        null=True,
        blank=True,
    )


# Create your models here.

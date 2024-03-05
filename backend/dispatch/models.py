from django.conf import settings
from django.db import models


class Dispatch(models.Model):
    "Generated Model"
    order = models.ForeignKey(
        "orders.Order",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="dispatch_order",
    )
    driver = models.ForeignKey(
        "authentication.Driver",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="dispatch_driver",
    )


# Create your models here.

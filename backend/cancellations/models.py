from django.conf import settings
from django.db import models


class Cancellation(models.Model):
    "Generated Model"
    order = models.ForeignKey(
        "orders.Order",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="cancellation_order",
    )
    reason = models.TextField()
    refund_issued = models.BooleanField()


# Create your models here.

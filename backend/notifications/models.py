from django.conf import settings
from django.db import models


class Notification(models.Model):
    "Generated Model"
    customer = models.ForeignKey(
        "authentication.Customer",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="notification_customer",
    )
    message = models.TextField()
    type = models.CharField(
        max_length=50,
    )
    read = models.BooleanField()


# Create your models here.

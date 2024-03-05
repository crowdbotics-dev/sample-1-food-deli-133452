from django.conf import settings
from django.db import models


class ChatSession(models.Model):
    "Generated Model"
    customer = models.ForeignKey(
        "authentication.Customer",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="chatsession_customer",
    )
    driver = models.ForeignKey(
        "authentication.Driver",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="chatsession_driver",
    )
    messages = models.JSONField()


# Create your models here.

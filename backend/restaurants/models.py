from django.conf import settings
from django.db import models


class Restaurant(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=255,
    )
    description = models.TextField()
    menu = models.JSONField()
    images = models.ImageField(
        null=True,
        blank=True,
        upload_to="restaurant_images/",
    )


# Create your models here.

from django.conf import settings
from django.db import models


class DriverReview(models.Model):
    "Generated Model"
    driver = models.ForeignKey(
        "authentication.Driver",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="driverreview_driver",
    )
    customer = models.ForeignKey(
        "authentication.Customer",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="driverreview_customer",
    )
    rating = models.IntegerField()
    comment = models.TextField(
        null=True,
        blank=True,
    )


class RestaurantReview(models.Model):
    "Generated Model"
    restaurant = models.ForeignKey(
        "restaurants.Restaurant",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="restaurantreview_restaurant",
    )
    customer = models.ForeignKey(
        "authentication.Customer",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="restaurantreview_customer",
    )
    rating = models.IntegerField()
    comment = models.TextField(
        null=True,
        blank=True,
    )


# Create your models here.

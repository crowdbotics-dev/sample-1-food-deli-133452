from rest_framework import serializers
from reviews.models import (
    DriverReview,
    RestaurantReview,
    DriverReview,
    RestaurantReview,
)


class DriverReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverReview
        fields = "__all__"


class RestaurantReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantReview
        fields = "__all__"

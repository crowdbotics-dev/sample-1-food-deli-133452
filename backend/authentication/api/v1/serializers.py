from rest_framework import serializers
from authentication.models import (
    Driver,
    RestaurantPartner,
    Customer,
    Customer,
    Driver,
    RestaurantPartner,
)


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = "__all__"


class RestaurantPartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantPartner
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

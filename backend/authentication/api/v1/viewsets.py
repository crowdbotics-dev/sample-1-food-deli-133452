from rest_framework import authentication
from authentication.models import (
    Driver,
    RestaurantPartner,
    Customer,
    Customer,
    Driver,
    RestaurantPartner,
    Customer,
    Driver,
    RestaurantPartner,
)
from .serializers import (
    DriverSerializer,
    RestaurantPartnerSerializer,
    CustomerSerializer,
    CustomerSerializer,
    DriverSerializer,
    RestaurantPartnerSerializer,
    CustomerSerializer,
    DriverSerializer,
    RestaurantPartnerSerializer,
)
from rest_framework import viewsets


class DriverViewSet(viewsets.ModelViewSet):
    serializer_class = DriverSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Driver.objects.all()


class RestaurantPartnerViewSet(viewsets.ModelViewSet):
    serializer_class = RestaurantPartnerSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = RestaurantPartner.objects.all()


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Customer.objects.all()

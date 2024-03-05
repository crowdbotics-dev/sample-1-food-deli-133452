from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    DriverViewSet,
    RestaurantPartnerViewSet,
    CustomerViewSet,
    CustomerViewSet,
    DriverViewSet,
    RestaurantPartnerViewSet,
    CustomerViewSet,
    DriverViewSet,
    RestaurantPartnerViewSet,
    CustomerViewSet,
    DriverViewSet,
    RestaurantPartnerViewSet,
)

router = DefaultRouter()
router.register("driver", DriverViewSet)
router.register("restaurantpartner", RestaurantPartnerViewSet)
router.register("customer", CustomerViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

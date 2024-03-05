from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    DriverReviewViewSet,
    RestaurantReviewViewSet,
    DriverReviewViewSet,
    RestaurantReviewViewSet,
    DriverReviewViewSet,
    RestaurantReviewViewSet,
    DriverReviewViewSet,
    RestaurantReviewViewSet,
)

router = DefaultRouter()
router.register("driverreview", DriverReviewViewSet)
router.register("restaurantreview", RestaurantReviewViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

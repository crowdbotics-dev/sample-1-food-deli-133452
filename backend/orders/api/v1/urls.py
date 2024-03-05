from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import OrderViewSet, OrderViewSet, OrderViewSet, OrderViewSet

router = DefaultRouter()
router.register("order", OrderViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

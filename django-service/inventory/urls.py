from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import InventoryViewSet, health_check


router = DefaultRouter()
router.register(r'', InventoryViewSet, basename='inventory')


urlpatterns = [
    path('health/', health_check, name='health-check'),
    path('', include(router.urls)),
]
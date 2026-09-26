from django.urls import path
from . import views

urlpatterns = [
    # Matches: GET /api/inventory/
    path('', views.inventory_list, name='inventory-list'),
    
    # Matches: GET /api/inventory/items/
    path('items/', views.inventory_list, name='inventory-items'),
    
    # Matches: GET /api/inventory/health/
    path('health/', views.health_check, name='health-check'),
]
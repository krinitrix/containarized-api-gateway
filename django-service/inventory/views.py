import socket

from django.db import connection
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import InventoryItem
from .serializers import InventoryItemSerializer


class InventoryViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all().order_by('id')
    serializer_class = InventoryItemSerializer


@api_view(['GET'])
def health_check(request):
    try:
        connection.ensure_connection()

        return Response({
            "status": "UP",
            "database": "CONNECTED",
            "service": "inventory-service",
            "server_id": "django-service",
            "container_id": socket.gethostname()
        })

    except Exception:
        return Response({
            "status": "DOWN",
            "database": "DISCONNECTED",
            "service": "inventory-service",
            "server_id": "django-service"
        }, status=status.HTTP_503_SERVICE_UNAVAILABLE)
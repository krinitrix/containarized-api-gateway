from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import socket
# Create your views here.
@api_view(['GET'])
def health_check(request):
    return Response({
        "status": "UP",
        "service": "inventory-service",
        "container_id": socket.gethostname()
    })
    
@api_view(['GET'])
def inventory_list(request):
    items=[
        {"id": 1, "sku": "SER-01", "name": "Cloud Node", "quantity": 12},
        {"id": 2, "sku": "SER-02", "name": "Load Balancer", "quantity": 4},
    ]
    return Response (
        {
            'items':items,
            'meta':{
                "service":"inventory-service",
                'container_id':socket.gethostname(),
            }
        }
    )
    

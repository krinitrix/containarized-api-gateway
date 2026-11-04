from django.contrib import admin
from .models import InventoryItem


@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sku', 'quantity', 'price')
    search_fields = ('name', 'sku')
    list_filter = ('created_at',)
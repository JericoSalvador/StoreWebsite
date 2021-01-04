from django.contrib import admin

# Register your models here.

from .models import Item, OrderItem, Order, Review

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Review)
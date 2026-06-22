from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'order_number',
        'user',
        'email',
        'total_price',
        'payment_status',
        'created_at',
    )

    list_filter = (
        'payment_status',
        'created_at',
    )

    search_fields = (
        'order_number',
        'user__username',
        'email',
    )

    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        'order',
        'product',
        'price',
    )
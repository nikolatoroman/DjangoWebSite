from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'platform',
        'price',
        'release_date',
        'is_available'
    )

    list_filter = (
        'platform',
        'is_available'
    )

    search_fields = ('title',)
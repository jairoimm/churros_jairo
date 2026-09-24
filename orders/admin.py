from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Order
from .models import OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "customer_name",
        "phone",
        "delivery_type",
        "total",
        "status",
        "created_at",
    )

    inlines = [OrderItemInline]


admin.site.register(OrderItem)

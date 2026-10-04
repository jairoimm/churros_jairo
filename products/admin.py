from django.contrib import admin

from .models import Product
from .models import Extra
from .models import ProductPortion

# Register your models here.

class ProductPortionInline(admin.TabularInline):
    model = ProductPortion
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'price', 'old_price', 'badge_text', 'active')
    search_fields = ('name',)
    inlines = [ProductPortionInline]

@admin.register(Extra)
class ExtraAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'price')

@admin.register(ProductPortion)
class ProductPortionAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'name', 'price', 'order', 'active')
    list_filter = ('product', 'active')
    
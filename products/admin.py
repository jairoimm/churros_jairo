from django.contrib import admin

from .models import Product
from .models import Extra

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'price', 'active')
    search_fields = ('name',)

@admin.register(Extra)
class ExtraAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'price')
    
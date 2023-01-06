from django.contrib import admin

from .models import Category, Product, Uom, Warehouse

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Uom)
admin.site.register(Warehouse)

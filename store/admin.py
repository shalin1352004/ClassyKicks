from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Brand, Product, ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ('name', 'brand', 'price', 'seller')

admin.site.register(Brand)
admin.site.register(Product, ProductAdmin)
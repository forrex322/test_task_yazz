from django.contrib import admin

from shops.models import Shop, Product, Category


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    search_fields = ["id", "name"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ["id", "name"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ["id", "name"]

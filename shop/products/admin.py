from django.contrib import admin
from products.models import Product, Purchase
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
   list_display = ("title", "price", "description", "created_at")
   fields = ("title", "price", "description", "created_at")
   readonly_fields = ("created_at",)
   search_fields = ("title", "price")

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "count")
    fields = ("user", "product", "count", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("user", "product")




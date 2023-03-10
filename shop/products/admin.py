from django.contrib import admin
from products.models import Product, Purchase
# Register your models here.

class PurchaseAdminInline(admin.StackedInline):
    model = Purchase

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
   list_display = ("title", "price", "description","color" ,"created_at")
   fields = ("title", "price", "description", "created_at")
   readonly_fields = ("created_at",)
   search_fields = ("title", "price")
   inlines = (PurchaseAdminInline,)


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "count","created_at")
    fields = ("user", "product", "count", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("user__email", "product__title")

from django.contrib import admin

# Register your models here.
from django.contrib import admin

from profiles.models import Profile
from products.models import Product

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
   list_display = ("user", "first_name", "last_name", "created_at")
   fields = ("user", "first_name", "last_name", "age","created_at")
   readonly_fields = ("created_at",)
   search_fields = ("first_name", "last_name")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
   list_display = ("title", "price", "description", "created_at")
   fields = ("title", "price", "description", "created_at")
   readonly_fields = ("created_at",)
   search_fields = ("title", "price")
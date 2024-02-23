from django.contrib import admin
from app_1.models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'add_date', 'image')
    ordering = (
    'name', 'price', 'description', 'add_date', 'image')  # order by name, price, description, add_date, image
    list_filter = (
    'name', 'price', 'description', 'add_date', 'image')  # filter by name, price, description, add_date, image
    search_fields = ('name', 'price', 'description', 'add_date', 'image')
    fieldsets = [
        (
            None,
            {
                "fields": ['name', 'price', 'add_date'],
            },
        ),
        (
            "Details",
            {
                "classes": ["collapse"],
                "fields": ["description", "image"],
            },
        ),
    ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'total_price', 'order_date')
    ordering = (
    'customer', 'total_price', 'order_date')  # order by customer, products, total_price, order_date
    list_filter = (
    'customer', 'total_price', 'order_date')  # filter by customer, products, total_price, order_date
    search_fields = ('customer', 'total_price', 'order_date')
    readonly_fields = ('order_date',)


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'address')
    ordering = ('name', 'email', 'phone_number', 'address')
    list_filter = ('name', 'email', 'phone_number', 'address')
    search_fields = ('name', 'email', 'phone_number', 'address')
    readonly_fields = ('name', 'email', 'phone_number', 'address')


admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)


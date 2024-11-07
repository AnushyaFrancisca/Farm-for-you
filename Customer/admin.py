from django.contrib import admin
from .models import  CartItem, Order

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'contact', 'location', 'total_price', 'order_date', 'display_products')
    
    # Method to display product names for an order
    def display_products(self, obj):
        return ", ".join([product.name for product in obj.products.all()])
    display_products.short_description = 'Products'  # Label for the column in admin
    
admin.site.register(Order, OrderAdmin)
admin.site.register(CartItem)  # Registering CartItem model if needed

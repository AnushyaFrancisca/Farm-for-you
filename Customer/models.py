from django.db import models
from Farmer.models import Product
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

# Create your models here.

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product, related_name='orders')  # Make it required

    def __str__(self):
        return f"Order by {self.user} on {self.order_date}"

class ProductSales(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)  # Each product has one sales record
    total_sold = models.PositiveIntegerField(default=0)  # Total quantity sold for this product

    def __str__(self):
        return f"{self.product.name} - Total Sold: {self.total_sold}"


from django.db import models
from Farmer.models import Product
from django.contrib.auth.models import User
import datetime

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
    contact = models.CharField(max_length=15)
    location = models.CharField(max_length=255)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)  # Correct usage of auto_now_add
    order_time = models.TimeField(default=datetime.time(12, 0))  # Correct default value (time object)
    products = models.ManyToManyField(Product)
    
    def __str__(self):
        return f"Order by {self.user.username} on {self.order_date}"

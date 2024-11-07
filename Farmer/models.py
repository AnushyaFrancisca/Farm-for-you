# models.py in your Django app (e.g., Farmer/models.py)

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class SensorData(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Temp: {self.temperature}, Humidity: {self.humidity}, Time: {self.timestamp}"

# Create your models here.

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    quantity = models.FloatField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.name

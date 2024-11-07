from django.contrib import admin
from .models import Product, SensorData

# Register your models here.

admin.site.register(Product)
admin.site.register(SensorData)

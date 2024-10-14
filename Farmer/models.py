# from django.db import models

# class Product(models.Model):
#     name = models.CharField(max_length=255)
#     quantity = models.FloatField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     image = models.ImageField(upload_to='products/')  # Ensure MEDIA_URL and MEDIA_ROOT are set in settings.py

#     def __str__(self):
#         return self.name

from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # To associate with the logged-in user
    name = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.name


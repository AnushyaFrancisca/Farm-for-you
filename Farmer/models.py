# from django.db import models
# from django.contrib.auth.models import User
# from Authenticate.models import userdetails
# # Create your models here.


# class Product(models.Model):
#     user = models.ForeignKey(userdetails, on_delete=models.CASCADE, related_name='products')  # Establishing relationship
#     name = models.CharField(max_length=255)
#     quantity = models.FloatField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     image = models.ImageField(upload_to='product_images/')  # Ensure Pillow is installed for ImageField

#     def __str__(self):
#         return self.name

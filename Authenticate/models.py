from django.db import models



from django.contrib.auth.models import User

# Create your models here.

class userdetails(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    user_phone = models.CharField(max_length=12)
    user_type = models.CharField(max_length=255)
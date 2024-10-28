from django.shortcuts import render
# views.py

from django.shortcuts import render
from Farmer.models import Product  # Assuming Product model holds product data

# Create your views here.

def profile(request):
    return render(request, 'Customer/profile.html')

def customer_market(request):
    products = Product.objects.all()  # Fetch all products
    return render(request, 'Customer/customer_market.html', {'products': products})

def cart(request):
    return render(request, 'Customer/cart.html')

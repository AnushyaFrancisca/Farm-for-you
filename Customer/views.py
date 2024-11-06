from django.shortcuts import render, redirect
# views.py

from django.shortcuts import render
from Farmer.models import Product  # Assuming Product model holds product data

# Create your views here.

def profile(request):
    return render(request, 'Customer/profile.html')

def customer_market(request):
    products = Product.objects.all()  # Fetch all products
    return render(request, 'Customer/customer_market.html', {'products': products})


from .models import CartItem
from Farmer.models import Product


def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'Customer/cart.html', {'cart_items': cart_items, 'total_price': total_price})

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, 
                                                       user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('view_cart')

def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('view_cart')


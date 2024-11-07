from django.shortcuts import render, redirect
from Farmer.models import Product  
from .models import CartItem, Order, ProductSales
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages


# Create your views here.

def profile(request):
    return render(request, 'Customer/profile.html')

def customer_market(request):
    products = Product.objects.all()  # Fetch all products
    return render(request, 'Customer/customer_market.html', {'products': products})

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
    return redirect('customer_market')

def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('view_cart')

@login_required
def confirm_order(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        location = request.POST.get('location')
        cart_items = CartItem.objects.filter(user=request.user)
        
        total_price = sum(item.product.price * item.quantity for item in cart_items)

        # Create the order
        order = Order.objects.create(
            user=request.user,
            name=name,
            contact=contact,
            location=location,
            total_price=total_price
        )
        
        # Add products from cart to the order and update stock
        for item in cart_items:
            order.products.add(item.product)  # Associate the product with the order

            # Optionally, update the product's stock
            product = item.product
            product.quantity -= item.quantity  # Reduce the stock by the quantity sold
            product.save()  # Save the updated product

            # Update the total sold quantity for the product
            product_sales, created = ProductSales.objects.get_or_create(product=item.product)
            product_sales.total_sold += item.quantity  # Add the quantity sold to the total
            product_sales.save()  # Save the updated sales record

        # Clear the cart after order is confirmed
        cart_items.delete()

        # Show a success message
        messages.success(request, f"Order confirmed for {name}. We will contact you at {contact}.")
        
        # Render the checkout page with a success message
        return render(request, 'Customer/checkout.html', {'order_confirmed': True})
    
    return redirect('view_cart')  # If it's not a POST request, redirect back to cart

def checkout(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        location = request.POST.get('location')

        # Here you can create the order or perform additional processing like sending confirmation emails.
        # For now, we'll just return a simple response:
        return HttpResponse(f"Order confirmed for {name} at {location}. We will contact you at {contact}.")
    
    return render(request, 'Customer/checkout.html')

@login_required
def user_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'customer/user_orders.html', {'orders': orders})

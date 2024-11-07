from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Product
from .forms import ProductForm
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.core.files.storage import default_storage
from .models import SensorData
import json
import os



# Create your views here.

def userpage(request):
    return render(request, 'Farmer/userpage.html')

def market_dashboard(request):
    return render(request, 'Farmer/market_dashboard.html')

@login_required(login_url='userlogin')
def seller_market(request):
    products = Product.objects.filter(user=request.user)  # Fetch products for the logged-in user
    context = {
        'products': products,  # Pass products to the template
    }
    return render(request, 'Farmer/market.html', context)

@login_required(login_url='userlogin')
def logout_farmer(request):
    auth_logout(request)
    return redirect('userlogin')

@csrf_exempt
@login_required
def market_view(request):
    if request.method == 'POST':
        product_name = request.POST.get('product-name')
        product_quantity = request.POST.get('product-quantity')
        product_price = request.POST.get('product-price')
        product_image = request.FILES.get('product-image')

        # Check if quantity and price are valid numbers
        if not product_quantity or not product_price:
            return JsonResponse({'status': 'error', 'message': 'Quantity and price are required'}, status=400)

        try:
            product_quantity = float(product_quantity)  # Convert to float
            product_price = float(product_price)  # Convert to float
        except ValueError:
            return JsonResponse({'status': 'error', 'message': 'Invalid quantity or price'}, status=400)

        user = request.user
        
        product = Product(
            name=product_name,
            quantity=product_quantity,
            price=product_price,
            image=product_image,
            user=user  # Associate the product with the user
        )
        product.save()

        return JsonResponse({'status': 'success', 'message': 'Product added successfully'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id, user=request.user)  # Check if the product belongs to the user
    if product.image:
        # Construct the full file path
        file_path = product.image.path
    if os.path.isfile(file_path):  # Check if the file exists
        default_storage.delete(file_path)  # Delete the file from storage

    product.delete()
    return redirect('market')   # Return a JSON response

# Create Product
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error', 'message': 'Invalid form data'})

def update_product(request, product_id):
    if request.method == 'POST':
        product = Product.objects.get(id=product_id)
        product.name = request.POST.get('edit-product-name')
        product.quantity = request.POST.get('edit-product-quantity')
        product.price = request.POST.get('edit-product-price')
        
        # If you handle images, you should save them as well
        if request.FILES.get('product-image'):
            product.image = request.FILES['product-image']
        
        product.save()
        
        return JsonResponse({'status': 'success'})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

def sensor_chart(request):
    # Sample data to be passed to the template
        # Get the latest sensor data
    # sensor_data = SensorData.objects.all().order_by('-timestamp')[:20]  # Last 20 entries
    # context = {
    #     'sensor_data': sensor_data,
    # }
    # return render(request, 'sensor_data/chart.html', context)
    context = {
        'temperature_data': [22, 23, 24],  # Dummy temperature data
        'humidity_data': [50, 55, 60],     # Dummy humidity data
        'timestamps': ['10:00', '10:01', '10:02']  # Sample timestamps
    }
    return render(request, 'Farmer/chart.html', context)

def save_sensor_data(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        temperature = data.get('temperature')
        humidity = data.get('humidity')

        # Save the data in the database
        sensor_data = SensorData(temperature=temperature, humidity=humidity)
        sensor_data.save()

        return JsonResponse({'status': 'success', 'message': 'Data saved successfully'})

    return JsonResponse({'status': 'fail', 'message': 'Invalid request'}, status=400)

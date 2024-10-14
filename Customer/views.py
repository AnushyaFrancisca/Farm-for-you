from django.shortcuts import render

# Create your views here.

def customer_market(request):
    return render(request, 'Customer/customer_market.html')


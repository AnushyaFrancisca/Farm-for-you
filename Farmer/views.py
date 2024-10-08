from django.shortcuts import render

# Create your views here.

def userpage(request):
    return render(request, 'Farmer/userpage.html')

def market_dashboard(request):
    return render(request, 'Farmer/market_dashboard.html')

def seller_market(request):
    return render(request, 'Farmer/market.html')
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def userpage(request):
    return render(request, 'Farmer/userpage.html')

def market_dashboard(request):
    return render(request, 'Farmer/market_dashboard.html')

def seller_market(request):
    return render(request, 'Farmer/market.html')

@login_required(login_url='userlogin')
def logout_farmer(request):
    auth_logout(request)
    return redirect('userlogin')
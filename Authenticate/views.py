from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password  # for encryption of password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import userdetails
from builtins import print
from django.views.generic import TemplateView

def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_active:
            if user.is_superuser:
                login(request, user)
                return redirect('admin-dashboard')

            details = userdetails.objects.get(user=user)

            if details.user_type == 'Official':
                login(request, user)
                return redirect('official-profile')

            elif details.user_type == 'Farmer':
                login(request, user)
                return redirect('userpage')

            elif details and details.user_type == 'Others':
                login(request, user)
                return redirect('others-profile')
            
        else:
            msg = "Wrong credentials"
            return render(request, 'Authenticate/login.html', {'msg': msg})
    return render(request, 'Authenticate/login.html')

def register(request):
    if request.method == 'POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        username = request.POST['username']  
        email = request.POST['email']
        phone = request.POST['phone']
        role = request.POST['role']
        password = request.POST['password1']
        
        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            msg = "Username already taken. Please choose another one."
            return render(request, 'Authenticate/Login.html', {'msg': msg})
        
        user = User(
            username=username,  # Include the username parameter
            email=email,
            password=make_password(password),
            first_name=firstName,
            last_name=lastName,
        )
        
        user.save()
        print(f"User created: {user.__dict__}")

        user_details = userdetails(user_id=user.id, user_phone=phone, user_type=role)
        user_details.save()

        return redirect('userlogin')

    return render(request, 'Authenticate/Login.html')

def about(request):
    return render(request, 'Authenticate/about.html')

def base(request):
    return render(request, 'Authenticate/Home.html')

def official(request):
    return render(request, 'official_dashboard.html')

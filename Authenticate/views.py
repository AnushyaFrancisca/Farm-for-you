from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password  # for encryption of password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import userdetails
from builtins import print
from django.views.generic import TemplateView
# from Farmer.models import Profile

# Create your views here.
def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user =  authenticate(request,username=username, password=password)
       
        

        if user is not None and user.is_active:

            if user.is_superuser:
                login(request, user)
                return redirect('admin-dashboard')

            details = userdetails.objects.get(user = user)
           
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
            msg = "wrong Credentials"
            return render(request, 'Authenticate/login.html', {'msg': msg})
    return render(request, 'Authenticate/login.html')


# def admin_dashboard(request):
#     # admin_dashboard.html needs to be added
#     return render(request, 'Admin/admin-dashboard.html')


def register(request):
    if request.method == 'POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        username = request.POST['username']  
        email = request.POST['email']
        phone = request.POST['phone']
        role = request.POST['role']
        password = request.POST['password1']
        
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
        user_model = User.objects.get(username=username)
        # new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
        # new_profile.save()
        # print(f"User details created: {user_details.__dict__}")


        return redirect('userlogin')

    return render(request, 'Authenticate/Login.html')


def about(request):
    return render(request, 'Authenticate/about.html')

def base(request):
    return render(request, 'Authenticate/Home.html')

def farmer(request):
    return render(request,'Farmer/userpage.html')

def official(request):
    return render(request, 'official_dashboard.html')
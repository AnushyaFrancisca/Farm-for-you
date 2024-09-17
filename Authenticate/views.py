from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request, 'Authenticate/home.html')

def about(request):
    return render(request, 'Authenticate/about.html')

def userlogin(request):
    return render(request, 'Authenticate/sign-in.html')

def register(request):
    return render(request, 'Authenticate/sign-up.html')
from django.urls import path
from Authenticate.views import *

urlpatterns = [
    path('',base,name='base'),
    path('Login',userlogin,name='login'),
    path('Authenticate/register',register,name='register'),
    path('Admin/about',about,name='about'),
]
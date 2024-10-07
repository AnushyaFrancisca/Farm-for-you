from django.urls import path
from Authenticate.views import *

urlpatterns = [
    path('',base,name='base'),
    path('Authenticate/Login',userlogin,name='userlogin'),
    path('Authenticate/register',register,name='register'),
    path('Admin/about',about,name='about'),
    path('dashboards/farmer_dashboard',farmer, name='farmer-profile'),
    path('dashboards/Offcial_Dashboard',official, name='official-profile'),
]
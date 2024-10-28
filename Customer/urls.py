from django.urls import path
from Customer.views import *

urlpatterns = [
    path('',profile,name='others-profile'),    
    path('customer_market/',customer_market,name='customer_market'),   
    path('cart/',cart,name='cart'),    
 
]
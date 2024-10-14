from django.urls import path
from Customer.views import *

urlpatterns = [
    path('', customer_market, name='customer_market'),  # Example URL pattern
]

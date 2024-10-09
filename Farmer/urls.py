from django.urls import path
from Farmer.views import *

urlpatterns = [
    path('',userpage,name='userpage'),
    path('dashboard/', market_dashboard, name='market_dashboard'),
    path('market/',seller_market,name='seller_market'),
    path('logout/',logout_farmer,name='logout_farmer'),
    
]
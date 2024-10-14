from django.urls import path
from Farmer.views import *

urlpatterns = [
    path('',userpage,name='userpage'),
    path('dashboard/', market_dashboard, name='market_dashboard'),
    path('market/',seller_market,name='market'),
    path('logout/',logout_farmer,name='logout_farmer'),
    # path('add-product/', add_product, name='add_product'),
    # path('edit-product/<int:product_id>/', edit_product, name='edit_product'),
    # path('delete-product/<int:product_id>/', delete_product, name='delete_product'),

    
]



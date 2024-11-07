from django.urls import path
from Farmer.views import *


urlpatterns = [
    path('',userpage,name='userpage'),
    path('dashboard/', market_dashboard, name='market_dashboard'),
    path('market/',seller_market,name='market'),
    path('logout/',logout_farmer,name='logout_farmer'),
    path('market/add/', market_view, name='market_view'),  # Updated to a unique URL pattern
    path('market/delete_product/<int:product_id>/', delete_product, name='delete_product'),
    path('create_product/', create_product, name='create_product'),
    path('update_product/<int:product_id>/', update_product, name='update_product'),
    path('api/save_sensor_data/', save_sensor_data, name='save_sensor_data'),
    path('chart/', sensor_chart, name='sensor_chart'), 
]



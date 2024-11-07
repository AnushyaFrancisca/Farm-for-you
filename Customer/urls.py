from django.urls import path
from Customer.views import *

urlpatterns = [
    path('', profile, name='others-profile'),
    path('customer_market/', customer_market, name='customer_market'),
    path('cart/', view_cart, name='view_cart'),
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('confirm_order/', confirm_order, name='confirm_order'),
    path('checkout/', checkout, name='checkout'),
    path('user/orders/', user_orders, name='user_orders'),
    ]

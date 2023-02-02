from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name = 'store'),
    path('search', views.search, name='search'),
    path('cart', views.cart, name = 'cart'),
    path('updatecart', views.updateCart, name = 'updatecart'),
    path('updatequantity', views.updateQuantity, name = 'updatequantity'),
    
]
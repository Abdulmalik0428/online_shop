from django.urls import path
from shop.views import home_view , product_view , products_view

urlpatterns = [
    path('', home_view , name='home'),
    path('product/<int:pk>/', product_view , name='product'),
    path('products/', products_view , name='products'),
]

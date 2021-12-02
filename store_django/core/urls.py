from django.contrib import admin
from django.urls import path
from .views import ProductsAPIView, ProductDetailOprs

urlpatterns = [
    path('products/', ProductsAPIView.as_view(), name='products'),
    path('products/add/', ProductsAPIView.as_view(), name='product-add'),
    path('products/detail/<int:pk>/', ProductDetailOprs.as_view(), name='product-detail'),
    path('products/update/<int:pk>/', ProductDetailOprs.as_view(), name='product-update'),
    path('products/delete/<int:pk>/', ProductDetailOprs.as_view(), name='product-delete'),
]


from django.contrib import admin
from django.urls import path
from katalog.views import product_list, main_view

app_name= 'katalog'

urlpatterns = [
    path('product-list/', product_list, name='product_list'),
    path('main-view/', main_view, name='main_view'),
  
]

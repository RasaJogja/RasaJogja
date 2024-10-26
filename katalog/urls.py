
from django.contrib import admin
from django.urls import path
from katalog.views import main_view

app_name= 'katalog'

urlpatterns = [
    path('main-view/', main_view, name='main_view'),
  
]

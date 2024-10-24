from django.urls import path
from autentikasi.views import show_main

app_name = 'autentikasi'

urlpatterns = [
    path('', show_main, name='show_main'),
]
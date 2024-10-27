from django.urls import path
from katalog import views  # Pastikan views diimpor dari aplikasi 'katalog'
from katalog.views import main_view

app_name = 'katalog'

urlpatterns = [
    path('main-view/', main_view, name='main_view'),
]

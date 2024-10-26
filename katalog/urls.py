from django.urls import path
from katalog import views  # Pastikan views diimpor dari aplikasi 'katalog'
from katalog.views import main_view

app_name = 'katalog'

urlpatterns = [
    path('products/', views.product_list, name='product_list'),  # URL untuk daftar produk
    path('main-view/', main_view, name='main_view'),
  
]

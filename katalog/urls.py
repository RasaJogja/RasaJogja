
from django.contrib import admin
from django.urls import path
from katalog import views  # Pastikan views diimpor dari aplikasi 'main'

app_name= 'katalog'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', views.product_list, name='product_list'),  # URL untuk daftar produk
    path('', views.product_list),  # URL root akan mengarah ke product_list
  

]

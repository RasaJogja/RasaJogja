"""
URL configuration for RasaJogja project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
<<<<<<< HEAD
# RasaJogja/urls.py
=======
>>>>>>> 517af474d0c1d6a73765c208c7d2e05365d1affe

from django.contrib import admin
from django.urls import path
from main import views  # Pastikan views diimpor dari aplikasi 'main'

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('products/', views.product_list, name='product_list'),  # URL untuk daftar produk
    path('', views.product_list),  # URL root akan mengarah ke product_list
=======
    
    
>>>>>>> 517af474d0c1d6a73765c208c7d2e05365d1affe
]

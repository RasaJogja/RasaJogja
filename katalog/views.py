# from django.shortcuts import render
# from .models import Product

# def main_view(request):
#     products = Product.objects.all()
#     return render(request, 'main.html', {'products': products})

import json
from django.shortcuts import render
from django.conf import settings
import os

def main_view(request):
    # Path ke file JSON
    file_path = os.path.join(settings.BASE_DIR, 'katalog', 'fixtures', 'products.json')
    
    # Memastikan file JSON ada
    if not os.path.exists(file_path):
        return render(request, 'product_list.html', {'products': [], 'error': 'File JSON tidak ditemukan.'})
    
    # Membaca data dari file JSON
    try:
        with open(file_path, 'r') as file:
            products = json.load(file)
    except json.JSONDecodeError:
        # Menangani kesalahan jika format JSON tidak valid
        return render(request, 'product_list.html', {'products': [], 'error': 'File JSON tidak valid.'})
    
    # Render ke template 'product_list.html' di dalam folder main/templates
    return render(request, 'product_list.html', {'products': products})
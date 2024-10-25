from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def main_view(request):
    products = Product.objects.all()
    return render(request, 'main.html', {'products': products})
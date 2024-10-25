from django.shortcuts import render
from .models import Product

def main_view(request):
    products = Product.objects.all()
    return render(request, 'main.html', {'products': products})
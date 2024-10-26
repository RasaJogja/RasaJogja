from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Bookmarks
from katalog.models import Product

@login_required
def add_bookmark(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    bookmark, created = Bookmarks.objects.get_or_create(user=request.user, product=product)

    if created:
        messages.success(request, f"{product.nama} di bookmark.")
    else:
        messages.info(request, f"{product.nama} sudah di bookmark.")
    return redirect('product_detail', product_id=product.id)

def remove_bookmark(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    bookmark = Bookmarks.objects.filter(user=request.user, product=product).first()

    if bookmark:
        bookmark.delete()
        messages.success(request, f"{product.nama} dihapus dari bookmark.")
    else:
        messages.info(request, f"{product.nama} belum di bookmark.")
    return redirect('product_detail', product)
# Create your views here.

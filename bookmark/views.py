from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Bookmarks
from katalog.models import Product
from django.http import JsonResponse

@login_required
def add_bookmark(request, product_id):
    if request.method == "POST":
        product = Product.objects.get(id=product_id)
        Bookmarks.objects.get_or_create(user=request.user, product=product)
        return JsonResponse({'status': 'added'})
    

def remove_bookmark(request, product_id):
    if request.method == "POST":
        Bookmarks.objects.filter(user=request.user, product_id=product_id).delete()
        return JsonResponse({'status': 'removed'})
# Create your views here.

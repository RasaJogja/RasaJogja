from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Product
from .models import Bookmarks
from katalog.models import Product
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import get_object_or_404

@csrf_exempt
@login_required
def remove_bookmark(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        user = request.user

        # Mencari atau membuat bookmark baru
        bookmark, created = Bookmarks.objects.get_or_create(user=user, product=product)

        if not created:
            # Jika bookmark sudah ada, hapus
            bookmark.delete()
            # is_bookmarked = False
            return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)
    
@csrf_exempt
@login_required
def add_bookmark(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user

    bookmark, created = Bookmarks.objects.get_or_create(user=user, product=product)

    if not created:
        # Jika bookmark sudah ada, hapus
        bookmark.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@csrf_exempt
@login_required
def bookmarked_products(request):
    bookmarks = Bookmarks.objects.filter(user=request.user)
    bookmarked_products = [bookmark.product for bookmark in bookmarks]

    return render(request, 'show_bookmarks.html', {'bookmarked_products': bookmarked_products})
    
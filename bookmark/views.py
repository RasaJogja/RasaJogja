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
def handle_bookmark(reqest, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = reqest.user

    bookmark, created = Bookmarks.objects.get_or_create(user=user, product=product)

    if not created:
        bookmark.delete()
    #     is_bookmarked = False
    # else:
    #     is_bookmarked = True
    return HttpResponseRedirect(reqest.META['HTTP_REFERER'])

@csrf_exempt
@login_required
def bookmarked_products(request):
    bookmarks = Bookmarks.objects.filter(user=request.user)
    bookmarked_products = [bookmark.product for bookmark in bookmarks]

    return render(request, 'show_bookmarks.html', {'bookmarked_products': bookmarked_products})
    

# def toggle_bookmark(request, product_id):
#     user = request.user
#     if user.is_authenticated:
#         if 'bookmarked_products' not in request.session:
#             request.session['bookmarked_products'] = []

#         # Tambah/hapus ID produk
#         if product_id in request.session['bookmarked_products']:
#             request.session['bookmarked_products'].remove(product_id)
#             status = 'removed'
#         else:
#             request.session['bookmarked_products'].append(product_id)
#             status = 'added'

#         # Save session
#         request.session.modified = True
#         return JsonResponse({'status': status})

#     return JsonResponse({'status': 'error', 'message': 'User not authenticated'}, status=403)
    
# def show_bookmarks(request):
#     # Produk yang ditampilkan di halaman
#     products = Product.objects.all() # ambil produk dari database
#     user_bookmarks = request.session.get('bookmarked_products', [])
    
#     return render(request, 'show_bookmarks.html', {
#         'products': products,
#         'user_bookmarks': user_bookmarks
#     })
# Create your views here.

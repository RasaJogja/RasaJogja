import json
from django.shortcuts import render, redirect, get_object_or_404 
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from review.models import ReviewEntry
from katalog.models import Product
from review.forms import ReviewEntryForm
from django.views.decorators.csrf import csrf_exempt

# Show Review View
@csrf_exempt
@login_required  
def show_review(request, pk):
    product = get_object_or_404(Product, pk=pk)
    order = request.GET.get('order', 'newest')  # Ambil parameter 'order' dari query string
    
    # Urutkan review berdasarkan parameter 'order'
    if order == 'oldest':
        reviews = ReviewEntry.objects.filter(product=product).select_related('user').order_by('time')
    else:  # default ke 'newest'
        reviews = ReviewEntry.objects.filter(product=product).select_related('user').order_by('-time')

    context = {
        'reviews': reviews,
        'product': product,
        'order': order  # Kirim parameter order ke template
    }
    return render(request, "page.html", context)

# Add Review View
@csrf_exempt
@login_required  
def add_review(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ReviewEntryForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review.review_text = review.review_text.replace("\r", "\n")  # Ganti \r dengan \n untuk line breaks
            review.save()

            # Mengembalikan respons JSON
            return JsonResponse({
                'username': review.user.username,
                'time': review.time.strftime("%B %d, %Y, %I:%M %p"),
                'review_text': review.review_text,
            })
        else:
            return HttpResponse("Form tidak valid", status=400)  # Mengembalikan HTTP 400 Bad Request

    # Jika bukan POST, render halaman add_review.html
    context = {
        'form': form,
        'product': product
    }
    return render(request, "add_review.html", context)

@csrf_exempt
def show_review_flutter(request, pk):
    product = get_object_or_404(Product, pk=pk)
    reviews = ReviewEntry.objects.filter(product=product).select_related('user')
    
    reviews_data = [{
        'pk': str(review.id),
        'fields': {
            'username': review.user.username,
            'time': review.time.strftime("%B %d, %Y, %I:%M %p"),
            'review_text': review.review_text,
        }
    } for review in reviews]
    
    product_data = {
        'pk': str(product.pk),
        'fields': {
            'nama': product.nama,
            'kategori': product.kategori,
            'harga': str(product.harga),
            'nama_restoran': product.nama_restoran,
        }
    }
    
    response_data = {
        'product': product_data,
        'reviews': reviews_data,
        'user_loggedin': request.user.username
    }
    return JsonResponse(response_data)

@csrf_exempt
def add_review_flutter(request):
    if request.method == 'POST':
        try:
            # Cek authentication
            if not request.user.is_authenticated:
                return JsonResponse({
                    'status': 'error',
                    'message': 'User must be logged in to submit review'
                }, status=401)

            data = json.loads(request.body)
            product_id = data.get('product_id')
            review_text = data.get('review_text')
            
            product = get_object_or_404(Product, pk=product_id)
            
            review = ReviewEntry.objects.create(
                user=request.user,
                product=product,
                review_text=review_text
            )
            
            return JsonResponse({
                'status': 'success',
                'review': {
                    'pk': str(review.id),
                    'fields': {
                        'user': review.user.id,
                        'username': review.user.username,
                        'product': review.product.id,
                        'product_name': review.product.name,
                        'time': review.time.strftime("%B %d, %Y, %I:%M %p"),
                        'review_text': review.review_text,
                    }
                }
            })
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=400)

    return JsonResponse({
        'status': 'error',
        'message': 'Invalid request method'
    }, status=400)

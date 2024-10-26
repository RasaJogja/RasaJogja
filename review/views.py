from django.shortcuts import render, redirect, get_object_or_404 
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from review.models import ReviewEntry
from katalog.models import Product
from review.forms import ReviewEntryForm

# Show Review View
@login_required  
def show_review(request, id):
    product = get_object_or_404(Product, pk=id)
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

# Create Review View
@login_required  
def add_review(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ReviewEntryForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
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

    context = {
        'form': form,
        'product': product
    }
    return render(request, "add_review.html", context)

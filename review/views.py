from django.shortcuts import render, redirect, get_object_or_404
from review.models import ReviewEntry
from katalog.models import Product
from review.forms import ReviewEntryForm


# Show Review View
def show_review(request, id):
    product = get_object_or_404(Product, pk=id)  # Gunakan get_object_or_404 agar aman jika produk tidak ditemukan
    reviews = ReviewEntry.objects.filter(product=product).select_related('user')
    context = {
        'reviews': reviews,
        'product': product
    }
    return render(request, "page.html", context)

# Create Review View
def add_review(request, id):
    product = get_object_or_404(Product, pk=id)  # Periksa apakah produk ada
    form = ReviewEntryForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        review = form.save(commit=False)
        review.user = request.user
        review.product = product
        review.review_text = review.review_text.replace("\r", "\n")  # Ganti \r dengan \n untuk line breaks
        review.save()
        return redirect('review:show_review', id=product.id)

    context = {
        'form': form,
        'product': product
    }
    return render(request, "add_review.html", context)

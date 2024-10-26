from django.urls import path
from bookmark.views import handle_bookmark, bookmarked_products

app_name = 'bookmark'

urlpatterns = [
    path('bookmark/<int:product_id>/', handle_bookmark, name='handle_bookmark'),
    path('bookmarked-products/', bookmarked_products, name='bookmarked_products'),
    # path('show-bookmarks', show_bookmarks, name='show_bookmarks'),  # URL untuk menampilkan daftar produk
    # path('toggle/<int:product_id>/', toggle_bookmark, name='toggle_bookmark'),  # URL untuk bookmark
    # # Tambahkan URL lainnya jika perlu
]
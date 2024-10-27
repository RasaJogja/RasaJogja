from django.urls import path
from bookmark.views import remove_bookmark, bookmarked_products, add_bookmark

app_name = 'bookmark'

urlpatterns = [
    path('bookmark/remove/<int:product_id>/', remove_bookmark, name='remove_bookmark'),
    path('bookmark/add/<int:product_id>/', add_bookmark, name='add_bookmark'),
    path('bookmarked-products/', bookmarked_products, name='bookmarked_products'),
]
from django.urls import path
from bookmark.views import *

urlpatterns = [
    path('add/<int:product_id>/', add_bookmark, name='add_bookmark'),
    path('remove/<int:product_id>/', remove_bookmark, name='remove_bookmark'),
]
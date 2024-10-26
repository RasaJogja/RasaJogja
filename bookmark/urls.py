from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:product_id>/', views.add_bookmark, name='add_bookmark'),
    path('remove/<int:product_id>/', views.remove_bookmark, name='remove_bookmark'),
]
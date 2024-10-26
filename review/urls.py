from django.urls import path
from . import views

app_name = 'review'
urlpatterns = [
    path('product/<int:pk>/', views.show_review, name='show_review'),
    path('product/<int:pk>/add/', views.add_review, name='add_review'),
]
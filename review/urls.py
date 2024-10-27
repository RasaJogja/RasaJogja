from django.urls import path
from review.views import show_review, add_review

app_name = 'review'
urlpatterns = [
    path('product/<int:pk>/', show_review, name='show_review'),
    path('product/<int:pk>/add/', add_review, name='add_review'),
]
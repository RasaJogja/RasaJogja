from django.urls import path
from review.views import add_review_flutter, show_review, add_review, show_review_flutter

app_name = 'review'
urlpatterns = [
    path('product/<int:pk>/', show_review, name='show_review'),
    path('product/<int:pk>/add/', add_review, name='add_review'),
    path('flutter/<int:pk>/', show_review_flutter, name='show_review_flutter'),
    path('flutter/add/', add_review_flutter, name='add_review_flutter'),

]
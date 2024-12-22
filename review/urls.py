from django.urls import path
from review.views import show_review, add_review, show_json_review

app_name = 'review'
urlpatterns = [
    path('product/<int:pk>/', show_review, name='show_review'),
    path('product/<int:pk>/add/', add_review, name='add_review'),
    path('show-json-review/', show_json_review, name='show_json_review'),
]
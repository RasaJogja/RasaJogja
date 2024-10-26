from django.urls import path
from . import views

app_name = 'review'
urlpatterns = [
    path('product/<int:id>/', views.show_review, name='show_review'),
    path('product/<int:id>/add/', views.add_review, name='add_review'),
]


# forum/urls.py
from django.urls import path
from . import views

app_name = 'forum'

urlpatterns = [
    path('forum-list/', views.forum_list, name='forum_list'),  # URL untuk daftar forum
    path('<uuid:forum_id>/', views.forum_detail, name='forum_detail'),  # URL untuk detail forum
    path('<uuid:forum_id>/threads/', views.thread_list, name='thread_list'),  # URL untuk daftar thread dalam forum
    path('threads/<uuid:thread_id>/', views.thread_detail, name='thread_detail'),  # URL untuk detail thread
    path('threads/<uuid:thread_id>/comments/', views.comment_list, name='comment_list'),  # URL untuk daftar komentar dalam thread
    path('create/', views.create_forum, name='create_forum'),  # URL untuk membuat forum baru
    path('<uuid:forum_id>/threads/create/', views.create_thread, name='create_thread'),  # URL untuk membuat thread baru dalam forum
    path('threads/<uuid:thread_id>/comments/create/', views.create_comment, name='create_comment'),  # URL untuk membuat komentar baru dalam thread
]
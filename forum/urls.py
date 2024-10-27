from django.urls import path
from forum.views import create_forum_entry, show_main, add_comment, delete_forum

app_name = 'forum'

urlpatterns = [
    path('show-main', show_main, name='show_main'),
    path('create-forum-entry/', create_forum_entry, name='create_forum_entry'),
    path('add-comment/<uuid:forum_entry_id>/', add_comment, name='add_comment'),
    path('delete/<uuid:id>', delete_forum, name='delete_forum'),
]

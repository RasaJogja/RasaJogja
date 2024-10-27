from django.urls import path
from forum.views import create_forum_entry,show_main
from forum.views import add_comment, add_forum_entry_ajax, delete_forum_entry

app_name = 'forum'

urlpatterns = [
    path('show-main', show_main, name='show_main'),  # Path kosong untuk halaman utama
    path('create-forum-entry/', create_forum_entry, name='create_forum_entry'),
    path('add-comment/<uuid:entry_id>/', add_comment, name='add_comment'),
    path('create-forum-entry-ajax', add_forum_entry_ajax, name='add_forum_entry_ajax'),
    path('delete_forum_entry/<int:forum_entry_id>/', delete_forum_entry, name='delete_forum_entry'),
]
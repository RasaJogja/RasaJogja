from django.urls import path
from chat.views import register, login_user, logout_user
from chat.views import show_main, create_chat, send_message, delete_message

app_name = 'chat'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-chat', create_chat, name='create_chat'),
    path('send-message/<uuid:chat_id>/', send_message, name='send_message'),
    path('delete-message/<uuid:message_id>', delete_message, name='delete_message'),
    
]
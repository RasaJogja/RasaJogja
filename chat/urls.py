from django.urls import path
from chat.views import create_chat, send_message, delete_message, handle_room

app_name = 'chat'

urlpatterns = [
    path('create-chat', create_chat, name='create_chat'),
    path('handle-room/<int:selected_user_id>', handle_room, name='handle_room'),
    path('send-message/<uuid:chat_id>/', send_message, name='send_message'),
    path('delete-message/<uuid:message_id>', delete_message, name='delete_message'), 
]
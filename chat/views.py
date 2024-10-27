from django.shortcuts import render, redirect, get_object_or_404
from chat.forms import ChatForm, MessageForm
from chat.models import Chat, Message
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from main.models import Profile
from django.contrib.auth.models import User

# Create your views here.

def create_chat(request):
    if(request.user.profile.role == "user"):
        user_valid = User.objects.filter(profile__role='seller')
    else:
        # If the current user is a seller, show users they have previously chatted with
        existing_chats = Chat.objects.all()
        users_selected = set()

        # Collect user IDs from chats the seller has participated in
        for chat in existing_chats:
            chat_users_set = set(chat.users.all())
            if request.user in chat_users_set:
                chat_users_set.remove(request.user)
                users_selected.update(user.id for user in chat_users_set)
        user_valid = User.objects.filter(id__in=users_selected)
    return render(request, 'create_chat.html', {'users': user_valid, 'user_loggedin':request.user, 'existing_messages':Message.objects.all().order_by('-timestamp')})


def handle_room(request, selected_user_id):
    # Retrieve the selected user by ID
    selected_user = get_object_or_404(User, id=selected_user_id)

    # Create a list of users that includes the selected user and the logged-in user
    all_users = [selected_user, request.user]

    # Check if a chat with these users already exists
    existing_chats = Chat.objects.filter(users__in=all_users).distinct()
    for chat in existing_chats:
        # Compare the users in each chat with the required users
        chat_users_set = set(chat.users.all())
        if chat_users_set == set(all_users):
            return redirect('chat:send_message', chat_id=chat.id)

    # Create a new chat if no existing chat is found
    chat = Chat.objects.create()
    chat.users.set(all_users)  # Add the users to the chat
    chat.save()

    # Redirect to the newly created chat
    return redirect('chat:send_message', chat_id=chat.id)

def send_message(request, chat_id):
    chat = get_object_or_404(Chat, pk=chat_id)

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.chat = chat  # Set the chat this message belongs to
            message.sender = request.user  # Set the current user as the sender
            message.save()
            
            # Return a JSON response with the message data
            return JsonResponse({
                'status': 'success',
                'message': {
                    'id': message.id,
                    'content': message.content,
                    'sender': message.sender.username,
                    'timestamp': message.timestamp.strftime('%Y-%m-%d %H:%M:%S')
                }
            })
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    else:
        form = MessageForm()

    return render(request, 'chat_detail.html', {'form': form, 'chat': chat})

def delete_message(request, message_id):
    # Get mood berdasarkan id
    message = Message.objects.get(pk=message_id)
    # Hapus mood
    message.delete()
    # Kembali ke halaman awal
    return redirect('chat:send_message', message.chat.id)

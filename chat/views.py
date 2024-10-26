from django.shortcuts import render, redirect, get_object_or_404
from chat.forms import ChatForm, MessageForm
from chat.models import Chat, Message
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

# Create your views here.

def create_chat(request):
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            # Get the selected users from the form
            selected_users = form.cleaned_data['users']

            # Create a list of users that includes the selected users plus the logged-in user
            all_users = list(selected_users)
            all_users.append(request.user)

            # Check if a chat with the same users already exists
            all_users_set = set(all_users)
            existing_chats = Chat.objects.filter(users__in=all_users).distinct()

            for chat in existing_chats:
                # Get the users in each chat and compare with the selected users plus the logged-in user
                chat_users_set = set(chat.users.all())
                if chat_users_set == all_users_set:
                    return redirect('chat:send_message', chat_id=chat.id)

            # If no existing chat is found, create a new chat
            chat = form.save(commit=False)
            chat.save()

            # Set the users including the logged-in user
            chat.users.set(all_users)

            # Redirect to the newly created chat
            return redirect('chat:send_message', chat_id=chat.id)
    else:
        form = ChatForm()

    return render(request, 'create_chat.html', {'form': form})


def send_message(request, chat_id):
    chat = Chat.objects.get(pk=chat_id)

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.chat = chat  # Set the chat this message belongs to
            message.sender = request.user  # Set the current user as the sender
            message.save()
            return redirect('chat:send_message', chat_id=chat.id)  # Redirect back to the chat page
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

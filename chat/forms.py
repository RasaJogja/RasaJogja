from django.forms import ModelForm
from chat.models import Chat, Message
from django import forms

class ChatForm(ModelForm):
    class Meta:
        model = Chat
        fields = ['users']
        widgets = {
            'users': forms.SelectMultiple(attrs={
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
            })
        }
    
    
class MessageForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
            'placeholder': 'Type your message...',
            'class': 'block mx-4 p-2 w-full h-10 text-sm text-gray-900 bg-white rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-800 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
        }))

    class Meta:
        model = Message
        fields = ['content']
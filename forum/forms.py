from django import forms
from .models import Forum, Thread, Comment

class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ['title', 'description']  # Field yang akan ditampilkan di form untuk membuat atau mengedit forum

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title']  # Field yang akan ditampilkan di form untuk membuat atau mengedit thread

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # Field yang akan ditampilkan di form untuk membuat atau mengedit komentar
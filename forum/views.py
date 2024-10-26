from django.shortcuts import render, get_object_or_404, redirect
from .models import Forum, Thread, Comment
from django.contrib.auth.decorators import login_required
from .forms import ThreadForm, CommentForm,ForumForm  # Asumsikan Anda memiliki form untuk thread dan komentar

def forum_list(request):
    forums = Forum.objects.all()
    return render(request, 'forum_list.html', {'forums': forums})

def forum_detail(request, forum_id):
    forum = get_object_or_404(Forum, id=forum_id)
    threads = forum.threads.all()  # Mendapatkan semua thread dalam forum ini
    return render(request, 'forum_detail.html', {'forum': forum, 'threads': threads})

@login_required
def thread_list(request, forum_id):
    forum = get_object_or_404(Forum, id=forum_id)
    threads = forum.threads.all()
    return render(request, 'thread_list.html', {'forum': forum, 'threads': threads})

@login_required
def thread_detail(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    comments = thread.comments.all()  # Mendapatkan semua komentar dalam thread ini
    return render(request, 'thread_detail.html', {'thread': thread, 'comments': comments})

@login_required
def create_thread(request, forum_id):
    forum = get_object_or_404(Forum, id=forum_id)
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.forum = forum
            thread.created_by = request.user
            thread.save()
            return redirect('forum:thread_detail', thread_id=thread.id)
    else:
        form = ThreadForm()
    return render(request, 'create_thread.html', {'form': form, 'forum': forum})

@login_required
def create_comment(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.thread = thread
            comment.created_by = request.user
            comment.save()
            return redirect('forum:thread_detail', thread_id=thread.id)
    else:
        form = CommentForm()
    return render(request, 'create_comment.html', {'form': form, 'thread': thread})

@login_required
def comment_list(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    comments = thread.comments.all()
    return render(request, 'comment_list.html', {'thread': thread, 'comments': comments})

def create_forum(request):
    if request.method == 'POST':
        form = ForumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forum:forum_list')  # Redirect ke daftar forum setelah berhasil membuat forum
    else:
        form = ForumForm()
    return render(request, 'create_forum.html', {'form': form})
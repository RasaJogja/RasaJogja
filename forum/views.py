from django.shortcuts import render, redirect, get_object_or_404
from forum.forms import ForumEntryForm, CommentForm
from forum.models import ForumEntry, Comment
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import HttpResponse

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    forum_entries = ForumEntry.objects.all()
    context = {
        'name': request.user.username,
        'forum_entries': forum_entries
    }
    return render(request, "forum.html", context)

@csrf_exempt
@require_POST
def add_forum_entry_ajax(request):
    title= request.POST.get("title")
    description = request.POST.get("description")
    user = request.user

    new_forum = ForumEntry(
        title=title, description=description,
        user=user
    )
    new_forum.save()

    return HttpResponse(b"CREATED", status=201)
def create_forum_entry(request):
    form = ForumEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        forum_entry = form.save(commit=False)
        forum_entry.user = request.user
        forum_entry.save()
        return redirect('forum:show_main')

    context = {'form': form}
    return render(request, "create_forum_entry.html", context)

@login_required
def add_comment(request, entry_id):
    forum_entry = get_object_or_404(ForumEntry, id=entry_id)
    
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Comment.objects.create(
                forum_entry=forum_entry,
                user=request.user,
                content=content
            )
            messages.success(request, 'Comment added successfully!')
        else:
            messages.error(request, 'Comment cannot be empty.')
    return redirect('forum:show_main')

@login_required
def delete_forum_entry(request, forum_id):
    forum_entry = get_object_or_404(ForumEntry, id=forum_id)
    # Check if the logged-in user is the author of the forum entry
    if request.user == forum_entry.author:
        forum_entry.delete()
        messages.success(request, "Forum entry deleted successfully.")
    else:
        messages.error(request, "You do not have permission to delete this entry.")
    
    return redirect('forum:show_main')  # Redirect to the forum list or appropriate page
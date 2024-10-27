from django.shortcuts import render, redirect, get_object_or_404, reverse
from forum.forms import ForumEntryForm, CommentForm
from forum.models import ForumEntry, Comment
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    forum_entries = ForumEntry.objects.all()
    context = {
        'name': request.user.username,
        'forum_entries': forum_entries
    }
    return render(request, "forum.html", context)


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
def add_comment(request, forum_entry_id):
    if request.method == 'POST':
        content = request.POST.get('content', '')
        forum_entry = get_object_or_404(ForumEntry, id=forum_entry_id)
        comment = Comment.objects.create(
            forum_entry=forum_entry,
            user=request.user,  # Use 'user' to match your model field
            content=content,
            created_at=timezone.now()
        )
        data = {
            'success': True,
            'comment': {
                'author': comment.user.username,
                'created_at': comment.created_at.strftime('%B %d, %Y, %I:%M %p'),
                'content': comment.content,
            },
            'answers_count': forum_entry.comments.count(),
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method.'})

@login_required
def delete_forum(request, id):
    forum = ForumEntry.objects.get(pk = id)
    forum.delete()
    return HttpResponseRedirect(reverse('forum:show_main'))
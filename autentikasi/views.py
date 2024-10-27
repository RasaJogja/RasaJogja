from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from autentikasi.forms import MoodEntryForm
from autentikasi.models import MoodEntry
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth import logout

@login_required(login_url='/login')
def show_main(request):
    mood_entries = MoodEntry.objects.all()

    context = {
        'name': 'Pak Bepe',
        'class': 'PBP D',
        'npm': '2306123456',
        'mood_entries': mood_entries
    }

    return render(request, "main.html", context)

def create_mood_entry(request):
    form = MoodEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('autentikasi:show_main')

    context = {'form': form}
    return render(request, "create_mood_entry.html", context)

def show_xml(request):
    data = MoodEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MoodEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = MoodEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = MoodEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register_user(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your user account has been successfully created!')
            return redirect('autentikasi:login_user')
    context = {'form': form, 'user_type': 'User'}
    return render(request, 'register.html', context)

def register_seller(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your seller account has been successfully created!')
            return redirect('autentikasi:login_seller')
    context = {'form': form, 'user_type': 'Seller'}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('autentikasi:show_main_user')
    else:
        form = AuthenticationForm(request)
    context = {'form': form, 'user_type': 'User'}
    return render(request, 'login.html', context)

def login_seller(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('autentikasi:show_main_seller')
    else:
        form = AuthenticationForm(request)
    context = {'form': form, 'user_type': 'Seller'}
    return render(request, 'login.html', context)

@login_required(login_url='/login_user')
def show_main_user(request):
    mood_entries = MoodEntry.objects.all()

    context = {
        'name': 'User Dashboard',
        'mood_entries': mood_entries
    }
    return render(request, "main_user.html", context)

@login_required(login_url='/login_seller')
def show_main_seller(request):
    mood_entries = MoodEntry.objects.all()

    context = {
        'name': 'Seller Dashboard',
        'mood_entries': mood_entries
    }
    return render(request, "main_seller.html", context)

def logout_user(request):
    logout(request)
    return redirect('autentikasi:login_user')

def logout_seller(request):
    logout(request)
    return redirect('autentikasi:login_seller')

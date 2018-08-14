from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django import forms
from django.views import View
from django.conf import settings
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Media, User
from .forms import LoginForm, SignUpForm, UploadForm
import requests

# Create your views here.


def index(request):
    media = Media.objects.all()
    return render(request, 'index.html', {'media': media})


def show(request, media_id):
    media = Media.objects.get(id=media_id)
    return render(request, 'show.html', {'media_id': media_id, 'media': media})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username=u, password=p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'You successfully logged in!')
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponseRedirect('/login')
            else:
                messages.error(request, 'Your username and/or password is incorrect.')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, 'You have signed up for Art Hub and are logged in!')
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    media = Media.objects.filter(user_id=user)
    return render(request, 'profile.html', {'username': username, 'media': media, })


@login_required
def upload(request, username):
    user = User.objects.get(username=username)
    media = Media.objects.filter(user_id_id=user.id)
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            print('user:', user, ' user_id: ', user.id)
            instance = Media(file=request.FILES['file'], user_id_id=user.id,
                             name=form.fields['name'], description=form.fields['description'])
            instance.save()
            messages.success(request, 'Your upload was successful!')
            return redirect('upload', username)
    else:
        form = UploadForm()
    return render(request, 'upload.html', {'form': form, 'username': username, 'media': media})


def like_img(request):
    media_id = request.GET.get('media_id', None)
    likes = 0
    if media_id:
        media = Media.objects.get(id=int(media_id))
        if media is not None:
            likes = media.likes + 1
            media.likes = likes
            media.save()
    return HttpResponse(likes)


def chat(request):
    return render(request, 'chat.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

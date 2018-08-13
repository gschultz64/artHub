from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django import forms
from django.views import View
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .models import Media
from .forms import *
import requests

# Create your views here.


def index(request):
    return render(request, 'index.html',)


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
                    return HttpResponseRedirect('/')
                else:
                    print("Account disabled")
                    return HttpResponseRedirect('/login')
            else:
                print("Username and/or password is incorrect")
        else:
            print("form is not valid")
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
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    media = Media.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'media': media,})


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            username = profile_form.cleaned_data.get('username')
            raw_password = profile_form.cleaned_data.get('password1')
            first_name = profile_form.cleaned_data.get('first_name')
            last_name = profile_form.cleaned_data.get('last_name')
            email = profile_form.cleaned_data.get('email')
            authenticate(username=username, password=raw_password,
                         first_name=first_name, last_name=last_name, email=email)
            return redirect('profile')
    else:
        profile_form = ProfileForm()
    return render(request, 'update_profile.html', {'profile_form': profile_form})


@login_required
def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload')
    else:
        form = UploadForm()
    return render(request, 'upload.html', {'form': form})


class BasicUploadView(View):
    def get(self, request):
        media_list = Media.objects.all()
        return render(self.request, 'media/basic_upload/index.html', {'media': media_list})

    def post(self, request):
        form = UploadForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            media = form.save()
            data = {'is_valid': True, 'name': media.file.name,
                    'url': media.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)


def forum(request):

    return render(request, 'forum.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

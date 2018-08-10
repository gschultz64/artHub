from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .models import Media
from .forms import LoginForm, SignUpForm, ProfileForm, UploadForm
import requests


# Create your views here.


def index(request):
    media = Media.objects.all()
    return render(request, 'index.html', {'media': media})


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
    # media = Media.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, })


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
            user = authenticate(username=username, password=raw_password,
                                first_name=first_name, last_name=last_name, email=email)
            return redirect('profile')
    else:
        profile_form = ProfileForm()
    return render(request, 'update_profile.html', {'profile_form': profile_form})


@login_required
def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST)
        # if form.is_valid():
        #     u = form.cleaned_data['username']
        #     p = form.cleaned_data['password']
        #     user = authenticate(username=u, password=p)
        #     if user is not None:
        #         if user.is_active:
        #             login(request, user)
        #             return HttpResponseRedirect('/')
        #         else:
        #             print("Account disabled")
        #             return HttpResponseRedirect('/login')
        #     else:
        #         print("Username and/or password is incorrect")
        # else:
        #     print("form is not valid")
    else:
        form = UploadForm()
    return render(request, 'upload.html')


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'test_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'test_upload.html')


def forum(request):

    return render(request, 'forum.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

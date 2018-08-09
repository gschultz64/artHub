from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Media
from .forms import LoginForm, SignUpForm
import requests

# Create your views here.


def index(request):
    media = Media.objects.all()
    return render(request, 'index.html', {'media': media})


def upload(request):

    return render(request, 'upload.html')

def forum(request):

    return render(request, 'forum.html')


@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    # media = Media.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, })


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


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

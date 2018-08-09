from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Media
from .forms import LoginForm
import requests

# Create your views here.


def index(request):
    return render(request, 'index.html',)


def upload(request):

    return render(request, 'upload.html')


@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    media = Media.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'media': media})


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
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

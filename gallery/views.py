from django.shortcuts import render
import requests
from django.http import HttpResponse
from django import forms

# Create your views here.


def index(request):
    return render(request, 'index.html',)


def upload_prompt(request):
    
    return render(request, 'upload.html')


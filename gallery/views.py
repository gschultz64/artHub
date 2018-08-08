import json
from django.shortcuts import render
import requests
from django.http import HttpResponse
from cloudinary.forms import cl_init_js_callbacks
from django import forms
from django.views.decorators.csrf import csrf_exempt
from .models import Photo
from .forms import PhotoDirectForm

# Create your views here.


def index(request):
    return render(request, 'index.html',)


def upload_prompt(request):
    context = dict(direct_form=PhotoDirectForm())
    cl_init_js_callbacks(context['direct_form'], request)
    return render(request, 'upload.html', context)


@csrf_exempt
def direct_upload_complete(request):
    form = PhotoDirectForm(request.POST)
    if form.is_valid():
        form.save()
        ret = dict(photo_id=form.instance.id)
    else:
        ret = dict(errors=form.errors)

    return HttpResponse(json.dumps(ret), content_type='application/json')

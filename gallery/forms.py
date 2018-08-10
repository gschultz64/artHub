from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Media

# forms


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(
        max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(
        max_length=100, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2', )


class ProfileForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=100)
    username = forms.CharField(label="Username", max_length=64)
    bio = forms.CharField(label='Bio', max_length=250)


class UploadForm(forms.ModelForm):
    link = forms.URLField(label='Image or Video URL',
                          max_length=255, help_text='Optional', required=False)

    class Meta:
        model = Media
        fields = ('name', 'description', 'file', 'link')

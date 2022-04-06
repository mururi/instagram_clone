from django import forms
from django.forms import ModelForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from insta.models import Image

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PostForm(ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
        exclude = ['profile']

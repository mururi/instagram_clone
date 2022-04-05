from django.shortcuts import render
from django.http import HttpResponse
from .models import Image
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

@login_required(login_url = 'accounts/login/')
def home(request):
    images = Image.get_images()
    return render(request, 'index.html', {"images": images})

def register(request):
    form = UserCreationForm
    return render(request, 'registration/register.html', {"form": form})
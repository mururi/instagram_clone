from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Image
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm, PostForm

@login_required(login_url = 'login/')
def home(request):
    images = Image.get_images()
    return render(request, 'index.html', {"images": images})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {"form": form})

@login_required(login_url = 'login/')
def create_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.profile = current_user.profile
            image.save()
        return redirect('home')
    else:
        form = PostForm()
    return render(request, 'create-post.html', {"form": form})
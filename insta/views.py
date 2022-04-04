from django.shortcuts import render
from django.http import HttpResponse
from .models import Image
from django.contrib.auth.decorators import login_required

@login_required(login_url = 'accounts/login/')
def home(request):
    images = Image.get_images()
    return render(request, 'index.html', {"images": images})

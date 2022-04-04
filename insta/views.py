from django.shortcuts import render
from django.http import HttpResponse
from .models import Image

def home(request):
    images = Image.get_images()
    return render(request, 'index.html', {"images": images})

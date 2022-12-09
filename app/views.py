from django.shortcuts import render, redirect
from .form import ImageForm
from .models import Image
from django.views import View
from django.contrib.staticfiles import finders

from .color_detection import get_image_hexcolors
from color_finder import settings

import os


# Create your views here.
def index(request):
    colors = []
    image = None

    if request.method == "POST":
        uploadImage = request.FILES.get("uploadImage")
        image = Image()
        image.image = uploadImage
        image.save()
        
        system_file_path = f"{settings.BASE_DIR.absolute()}{image.image.url}"
        hex_colors = get_image_hexcolors(system_file_path)
        print(hex_colors)
        colors = hex_colors

    context = {
        "colors":colors,
        "image":image
    }
    return render(request,"index.html",context=context)


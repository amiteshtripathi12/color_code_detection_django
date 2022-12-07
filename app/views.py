from django.shortcuts import render, redirect
from collections import Counter
from sklearn.cluster import KMeans
from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
from .form import ImageForm
from .models import Image
from django.views import View

# Create your views here.
def index(request):
    if request.method == "POST":
        form = ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            return render(request,"index.html",{"obj":obj})
    else:
        form = ImageForm()
        #img = Image.objects.all()
    return render(request,"index.html",{"form":form})


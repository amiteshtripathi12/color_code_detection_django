from django.db import models

# Create your models here.

class Image(models.Model):
    objects = None
    image = models.ImageField(upload_to='uploads/photos')
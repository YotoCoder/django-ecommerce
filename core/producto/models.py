from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Producto(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    description = models.CharField(max_length=500)
    color = models.CharField(max_length=30)
    img = models.ImageField(upload='img/products')
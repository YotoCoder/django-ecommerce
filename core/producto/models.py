from distutils.command.upload import upload
from importlib.metadata import requires
from random import choices
from secrets import choice
from unicodedata import category
from django.db import models

# Create your models here.

stars = ( 
    (1, 1), 
    (2, 2), 
    (3, 3), 
    (4, 4), 
    (5, 5),
) 

class Producto(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    description = models.CharField(max_length=500)
    code = models.CharField(max_length=50)
    color = models.CharField(max_length=30)
    img = models.ImageField(upload_to='img/productos/', blank=True)
    offer = models.CharField(max_length=30)
    in_stock = models.IntegerField()
    category = models.CharField(max_length=30)

    clasification = models.IntegerField(choices=stars)

    def __str__(self):
        return self.name

class Index(models.Model):
    product = models.ManyToManyField('Producto')
    
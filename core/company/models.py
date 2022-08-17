from pyexpat import model
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name    

class Currency(models.Model):
    money_simbol = models.TextField(max_length=10)


class Company(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=25)
    logo = models.ImageField(upload_to='img/productos/', blank=True)
    
    color = models.CharField(max_length=30)
    about_me = models.TextField(max_length=255)

    currency = models.CharField(max_length=10)

    category = models.ManyToManyField('Category')

    address = models.CharField(max_length=25)
    facebook = models.URLField()
    twitter = models.URLField()
    instagram = models.URLField()

    def __str__(self):
        return self.name
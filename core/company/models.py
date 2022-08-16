from django.db import models

# Create your models here.

class Company(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=25)
    logo = models.ImageField(upload_to='media/img/productos', blank=True)
    currency = models.CharField(max_length=2)
    
    address = models.CharField(max_length=25)
    facebook = models.URLField()
    twitter = models.URLField()
    instagram = models.URLField()

    def __str__(self):
        return self.name
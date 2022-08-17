from django.contrib import admin
from .models import Company, Category, Currency

# Register your models here.

admin.site.register(Company)
admin.site.register(Category)
admin.site.register(Currency)
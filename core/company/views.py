from django.shortcuts import render
from django.views.generic import View
from .models import Company

# Create your views here.


class CompanyView(View):
    model = Company
    template_name = 'templates/index.html'
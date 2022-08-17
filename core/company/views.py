from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views import View
from .models import Company

# Create your views here.


class CompanyView(View):
    model = Company
    template_name = 'templates/base.html'
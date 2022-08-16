from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Company

# Create your views here.


class CompanyView(DetailView):
    model = Company
    template_name = 'templates/base.html'
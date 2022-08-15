from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

# Create your views here.

class Inicio(TemplateView):

    template_name = 'templates/index.html'

class Test(TemplateView):

    template_name = 'templates/test.html'

class ProductDetail(TemplateView):

    template_name = 'templates/product.html'
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Producto

# Create your views here.

class Inicio(TemplateView):

    template_name = 'templates/index.html'

class Test(TemplateView):

    template_name = 'templates/test.html'

class ProductDetail(DetailView):

    model = Producto
    template_name = 'templates/product.html'
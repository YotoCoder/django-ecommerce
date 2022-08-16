from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, CreateView, ListView
from .models import Producto
from .forms import ProductForm

# Create your views here.

class Inicio(TemplateView):

    template_name = 'templates/index.html'

class Test(TemplateView):

    template_name = 'templates/test.html'


class ProductList(ListView):
    model = Producto
    template_name = 'templates/product_list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['headlines'] = self.model._meta.get_fields()
        return context

class ProductDetail(DetailView):

    model = Producto
    template_name = 'templates/product.html'

class CreateProduct(CreateView):

    model = Producto
    template_name = 'templates/create_product.html'
    form = ProductForm
    fields = '__all__'
    success_url = 'list-products'


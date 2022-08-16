from ast import For
from django.forms import ModelForm
from .models import Producto

class ProductForm(ModelForm):
    model = Producto
    
"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from producto.views import Inicio, Test, ProductDetail, CreateProduct, ProductList
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Inicio.as_view()),
    path('test', Test.as_view()),
    path('product/<slug:pk>', ProductDetail.as_view()),
    path('create-product', CreateProduct.as_view()),
    path('product-list', ProductList.as_view(), name='product-list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

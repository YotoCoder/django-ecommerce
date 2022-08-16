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
from django.urls import path, include
from producto.views import ProductDetail, CreateProduct, ProductList, UpdateProduct, DeleteProduct
from django.conf import settings
from django.conf.urls.static import static
from company.views import CompanyView

urlpatterns = [
    path('', CompanyView.as_view()),
    path('admin/', admin.site.urls),
    path('product-detail/<slug:pk>', ProductDetail.as_view()),
    path('create-product', CreateProduct.as_view()),
    path('product-list', ProductList.as_view(), name='product-list'),
    path('update-product/<int:pk>', UpdateProduct.as_view()),
    path('delete-product/<slug:pk>', DeleteProduct.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

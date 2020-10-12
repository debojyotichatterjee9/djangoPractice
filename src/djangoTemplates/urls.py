"""djangoTemplates URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from pages.views import home_page_view, about_page_view, contact_page_view
from products.views import product_detail_view, product_create_view, product_delete_view, product_list_view, product_update_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page_view, name='home'),
    path('about/', about_page_view, name='about'),
    path('contact/', contact_page_view, name='contact'),
    path('product/details/<str:product_id>', product_detail_view, name='details'),
    path('product/create', product_create_view, name='create'),
    path('product/delete/<product_id>', product_delete_view, name='delete'),
    path('product/list', product_list_view, name='list'),
    path('product/update/<product_id>', product_update_view, name='update'),
]

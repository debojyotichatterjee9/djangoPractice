"""djangoPractice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from pages import views
from product.views import product_detail_view, product_create_view, product_create_view_two, google_search_view, product_create_view_three, product_update_view, product_delete_view, product_list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home_view, name="home"),
    path('social/', views.social_view, name="social"),
    path('about/', views.about_view, name="about"),
    path('contact/', views.contact_view, name="contact"),
    path('product/<int:pid>/', product_detail_view, name="product"),
    path('product/create/', product_create_view, name="create"),
    path('product/create_two/', product_create_view_two, name="create_two"),
    path('product/create_three/', product_create_view_three, name="create_three"),
    path('product/update/<int:pid>/', product_update_view, name="product_update"),
    path('product/<int:pid>/delete/', product_delete_view, name="product_delete"),
    path('productList/', product_list_view, name="product_list"),
    path('product/google_search/', google_search_view, name="google_search")
]

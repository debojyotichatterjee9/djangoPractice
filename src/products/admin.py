from django.contrib import admin

# COMMENT: This is called a relative import
from .models import Product

# Register your models here.
admin.site.register(Product)
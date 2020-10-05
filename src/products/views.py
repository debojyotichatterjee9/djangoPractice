from django.shortcuts import render
from .models import Product
# Create your views here.

def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     "title": obj.title,
    #     "description": obj.description,
    #     "price": obj.price,
    #     "summary": obj.summary,
    #     "available": obj.available
    # }
#     For better usability changing the context and mapping to the product object
    context = {
        "product": obj
    }
    return render(request, "products/products_detail.html", context)
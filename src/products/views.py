from django.shortcuts import render
from .models import Product
from .forms import ProductForm
# Create your views here.


''' ==================================== PRODUCT DETAIL VIEW ==================================== '''
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


''' ==================================== PRODUCT CREATE VIEW ==================================== '''
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        "form": form
    }
    return render(request, "products/products_create.html", context)
from django.shortcuts import render
from .models import Product
from .forms import ProductForm, RawProductForm
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
# ~~~~~~~~~~ FOR DJANGO MODEL FORM METHOD ~~~~~~~~~~
# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()
#     context = {
#         "form": form
#     }
#     return render(request, "products/products_create.html", context)

# ~~~~~~~~~~ FOR RAW HTML FORM METHOD ~~~~~~~~~~
# def product_create_view(request):
#     if request.method == 'POST':
#         userInput = {
#         'title': request.POST.get('title'),
#         'description': request.POST.get('description'),
#         'summary': request.POST.get('summary'),
#         'price': request.POST.get('price'),
#         'available': request.POST.get('available')
#         }
#         if userInput['available'] is None:
#             userInput['available'] = False
#         print(userInput)
#         if userInput:
#                Product.objects.create(**userInput)
# #             Product.objects.create(title = userInput['title'],
# #                            description = userInput['description'],
# #                            summary = userInput['summary'],
# #                            price = userInput['price'],
# #                            available = userInput['available'])
#     context = {
#         
#     }
#     return render(request, "products/products_create.html", context)

# ~~~~~~~~~~ FOR PURE DJANGO FORM METHOD ~~~~~~~~~~
def product_create_view(request):
    form = RawProductForm()
    if request.method == 'POST':
        form = RawProductForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Product.objects.create(**form.cleaned_data)
            form = RawProductForm()
        else:
            print(form.errors)
    context = {
        'form': form
    }
    return render(request, "products/products_create.html", context)
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Product
from .forms import ProductForm, RawProductForm
# Create your views here.


''' ==================================== PRODUCT DETAIL VIEW ==================================== '''
def product_detail_view(request, product_id):
    # this is a simpler way of getting the default Django 404 page
    # obj = get_object_or_404(Product, id=int(product_id))
    # we can also use the try catch method and raise Http404 error which does the same
    try:
        obj = Product.objects.get(pk=product_id)
    except:
        raise Http404
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
    # setting initial data for the form
    initial_data = {
        "price": 299.99
    }
    form = RawProductForm(initial=initial_data)
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


''' ==================================== PRODUCT DELETE VIEW ==================================== '''
def product_delete_view(request, product_id):
    queryset = Product.objects.filter(available=True) # filtering the items with available=True
    obj = get_object_or_404(queryset, pk=product_id)
    if(request.method == 'POST'):
        obj.available = False # doing a soft delete and saving the updated the data
        obj.save()
        return redirect('../list')
    context = {
        "product": obj
    }
    return render(request, "products/products_delete.html", context)


''' ==================================== PRODUCT LIST VIEW ==================================== '''
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "product_list": queryset
    }
    return render(request, "products/products_list.html", context)
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Product
from .forms import ProductForm, RawProductForm
# Create your views here.

def product_detail_view(request, pid):

    # obj = Product.objects.get(id=pid) # this is the normal way of query
    # obj = get_object_or_404(Product, id=pid) #this will handle the wrong id in the url and get a 404 page
# following is another method of renedring the 404 page, above two menthods are valid too..
    try:
        obj = Product.objects.get(id=pid)
    except Product.DoesNotExist:
        raise Http404

    # context = {
    #     "title": obj.title,
    #     "description": obj.description,
    #     "price": obj.price,
    #     "summary": obj.summary,
    #     "featured": obj.featured
    # }
    context = {
        "object": obj
    }
    return render(request, "product/product_detail.html", context)
    # this is rendered from inside the products folder, now since
    # we have mentioned in the settings.py under DIR that the path to look into
    # should be
    # os.path.join(BASE_DIR, "templates") which is C:\Users\debojyotichatterjee\Documents\practiceProjects\djangoPractice\source\templates
    # django will first look for the template in the above mentioned path. If not found then it will look into admin templates folder
    # and finally inside the app folder.
    # So here django first searches inside the above mentioned path, does not find it there and then looks inside the app folder path
    # to render it from there if the file is found. Otherwise it throws an error.


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        "form": form
    }
    return render(request, "product/product_create.html", context)

def product_create_view_two(request):
    if request.method == 'POST':
        my_new_title = request.POST.get('title')
        print(my_new_title)
    context = {}
    return render(request, "product/product_create_two.html", context)

def product_create_view_three(request):
    product_form = RawProductForm()
    if request.method == 'POST':
        product_form = RawProductForm(request.POST)
        if product_form.is_valid():
            # now the data in the form is valid(well, almost)
            print(product_form.cleaned_data)
            Product.objects.create(**product_form.cleaned_data) #this will save the data and the arguement passed will make it a dict(this command can be run in the shell too)
        else:
            print(product_form.errors)
    context = {
        "form": product_form
    }
    return render(request, "product/product_create_three.html", context)

def product_update_view(request, pid):
    initial_data = {
        'title': "Product Title",
        'description': "Product Description",
        'price': "0.00",
        'summary': "Product Summary",
        'featured': False
    }
    # obj = Product.objects.get(id=pid) # this is the normal way of query
    obj = get_object_or_404(Product, id=pid) #this will handle the wrong id in the url and get a 404 page
    form = ProductForm(request.POST or None,
                        # initial=initial_data, # we do not need to set the initial data for this form
                        instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "product/product_update.html", context)

def product_delete_view(request, pid):
    obj = get_object_or_404(Product, id=pid)
    if request.method == "POST":
        obj.delete() #just confirming to delete
        return redirect("../../google_search/") #after deleteing product redirecting to the google search form
    context = {
        "object": obj
    }
    return render(request, "product/product_delete.html", context)

def product_list_view(request):
    queryset = Product.objects.all() #this will give us a list of objects from the database
    context = {
        "object_list": queryset
    }
    return render(request, "product/product_list.html", context)

def google_search_view(request):
    context = {}
    return render(request, "product/google_search_form.html", context)

from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import User
from .forms import UserForm


''' ==================================== USER LIST VIEW ==================================== '''
def user_list_view(request):
    queryset = User.objects.all()
    context = {
        "user_list": queryset
    }
    return render(request, "users/users_list.html", context)


''' ==================================== USER DETAIL VIEW ==================================== '''
def user_detail_view(request, user_id):
    # this is a simpler way of getting the default Django 404 page
    # obj = get_object_or_404(Product, id=int(product_id))
    # we can also use the try catch method and raise Http404 error which does the same
    try:
        obj = User.objects.get(pk=user_id)
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
        "user": obj
    }
    return render(request, "users/users_detail.html", context)
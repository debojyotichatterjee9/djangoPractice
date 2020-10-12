from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)
from django.http import Http404
from .models import User
from .forms import UserForm


''' ==================================== USER LIST VIEW ==================================== '''
# def user_list_view(request):
#     queryset = User.objects.all()
#     context = {
#         "user_list": queryset
#     }
#     return render(request, "users/users_list.html", context)

class UserListView(ListView):
    # by default django class based view will search this loaction -> <users>/<model_name>_list.html
    # but we can provide our own template in custom path
    template_name = "users/users_list.html"
    queryset = User.objects.all()


''' ==================================== USER DETAIL VIEW ==================================== '''
def user_detail_view(request, user_id):
    # this is a simpler way of getting the default Django 404 page
    # obj = get_object_or_404(Product, id=int(product_id))
    # we can also use the try catch method and raise Http404 error which does the same
    try:
        obj = User.objects.get(pk=user_id)
    except:
        raise Http404
    context = {
        "user": obj
    }
    return render(request, "users/users_detail.html", context)
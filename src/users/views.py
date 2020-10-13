from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
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

''' ==================================== USER CREATE VIEW ==================================== '''
class UserCreateView(CreateView):
    template_name = "users/users_create.html"
    form_class = UserForm
    # queryset = User.objects.all()
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
    # this method can override the get_absolute_url function and lets you define a path after success
    def get_success_url(self):
        return "/user/list"
    
    
    
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
# def user_detail_view(request, user_id):
#     # this is a simpler way of getting the default Django 404 page
#     # obj = get_object_or_404(Product, id=int(product_id))
#     # we can also use the try catch method and raise Http404 error which does the same
#     try:
#         obj = User.objects.get(pk=user_id)
#     except:
#         raise Http404
#     context = {
#         "user": obj
#     }
#     return render(request, "users/users_detail.html", context)

class UserDetailView(DetailView):
    # by default django class based view will search this loaction -> <users>/<model_name>_list.html
    # but we can provide our own template in custom path
    template_name = "users/users_detail.html"
    # this queryset basically limits the result in which the details is searched
    # but if you are overriding the keyword search like below then it would not work
    queryset = User.objects.filter(deleted=False)
    #class based view searches with the keyword pk but we are overriding it using user_id
    def get_object(self):
        user_id = self.kwargs.get("user_id")
        return get_object_or_404(User, id=user_id)
    
    
''' ==================================== USER UPDATE VIEW ==================================== '''
class UserUpdateView(UpdateView):
    template_name = "users/users_update.html"
    form_class = UserForm
    # queryset = User.objects.all()
    
    def get_object(self):
        user_id = self.kwargs.get("user_id")
        return get_object_or_404(User, id=user_id)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
    # this method can override the get_absolute_url function and lets you define a path after success
    def get_success_url(self):
        return reverse("users:list")
    
    
    ''' ==================================== USER DELETE VIEW ==================================== '''
class UserDeleteView(DeleteView):
    template_name = "users/users_delete.html"
    def get_object(self):
        user_id = self.kwargs.get("user_id")
        return get_object_or_404(User, id=user_id)
    
    def get_success_url(self):
        return reverse("users:list")
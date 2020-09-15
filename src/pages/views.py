from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

''' ==================================== HOME PAGE VIEW ==================================== '''
def home_page_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World!!</h1>")
        return render(request, 'home.html', {})


''' ==================================== ABOUT PAGE VIEW ==================================== '''
def about_page_view(request, *args, **kwargs):
    # return HttpResponse("<h1>About Page</h1>")
    return render(request, 'about.html', {})


''' ==================================== CONTACT PAGE VIEW ==================================== '''
def contact_page_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Contact Page</h1>")
    return render(request, 'contact.html', {})
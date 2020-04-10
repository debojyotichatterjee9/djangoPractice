from django.shortcuts import render

# Create your views here.
def myfbv(request, *args, **kwargs):
    return render(request, 'about.html', {})

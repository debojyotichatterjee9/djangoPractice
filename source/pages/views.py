from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    # return HttpResponse("<h1>This is Home View</h1>")
    return render(request, 'home.html', {})
    pass

def social_view(request, *args, **kwargs):
    # return HttpResponse("<h1>This is Social View</h1>")
    return render(request, 'social.html', {})
    pass

def about_view(request, *args, **kwargs):
    # return HttpResponse("<h1>This is About View</h1>")
    my_contex = {
        "my_text": "this is a text material that passed as a context to the About Page template.",
        "my_number": 8402384038427423,
        "my_list": ["Fred","Mike","Dorothy","Cynthia","Beth","Kevin","Tom","Jaquline","Martha", 995, 660],
        "my_html1": "<div><h3>This is a raw HTML passed with |safe filter.</h3></div>",
        "my_html2": "<div><h3>This is a raw HTML passed with |striptags filter.</h3></div>"
    }
    return render(request, 'about.html', my_contex)
    pass

def contact_view(request, *args, **kwargs):
    # return HttpResponse("<h1>This is Contact View</h1>")
    return render(request, 'contact.html', {})
    pass

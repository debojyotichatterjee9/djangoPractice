from django.shortcuts import render
from django.views import View

# BASE VIEW CLASS = VIEW

class JobView(View):
    template_name = 'job/job_list.html'
    def get(self, request, id=None, *args, **kwargs):
        return render(request, self.template_name, {})

# Create your views here.
def myfbv(request, *args, **kwargs):
    return render(request, 'contact.html', {})

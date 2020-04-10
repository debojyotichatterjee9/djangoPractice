from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Job
from .forms import JobModelForm
# BASE VIEW CLASS = VIEW

# =========================== DETAIL VIEW =========================== #
class JobView(View):
    template_name = 'job/job_detail.html'
    def get(self, request, id=None, *args, **kwargs):
        context = {}
        if id is not None:
            obj = get_object_or_404(Job, id=id)
            context['object'] = obj
        return render(request, self.template_name, context)

# Create your views here.
def myfbv(request, *args, **kwargs):
    return render(request, 'contact.html', {})


# =========================== LIST VIEW =========================== #
class JobListView(View):
    template_name = 'job/job_list.html'
    queryset = Job.objects.all()

    def get_query_set(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {
            'object_list': self.get_query_set()
            }
        return render(request, self.template_name, context)


# =========================== CREATE VIEW =========================== #
class JobCreateView(View):
    template_name = 'job/job_create.html'
    # GET METHOD
    def get(self, request, *args, **kwargs):
        form = JobModelForm()
        context = {
            "form": form
        }
        return render(request, self.template_name, context)

    # POST METHOD
    def post(self, request, *args, **kwargs):
        form = JobModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/job") # this will redirect the url after save is successful
        context = {
            "form": form
        }
        return render(request, self.template_name, context)

from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Job
from .forms import JobModelForm
# BASE VIEW CLASS = VIEW




# =========================== JOB OBJECT MIXIN VIEW =========================== #
class JobObjectMixinView(object):
    model = Job
    lookup = 'id'
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id=id)
        return obj




# =========================== DETAIL VIEW =========================== #
class JobView(JobObjectMixinView, View):
    template_name = 'job/job_detail.html'
    def get(self, request, id=None, *args, **kwargs):
        context = {'object': self.get_object()}

        return render(request, self.template_name, context)

# Create your views here.
def myfbv(request, *args, **kwargs):
    return render(request, 'contact.html', {})

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
            return redirect("/job/") # this will redirect the url after save is successful
        context = {
            "form": form
        }
        return render(request, self.template_name, context)


# =========================== UPDATE VIEW =========================== #
class JobUpdateView(JobObjectMixinView, View):
    template_name = 'job/job_update.html'

    #  GET METHOD
    def get(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = JobModelForm(instance=obj)
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

    # POST METHOD
    def post(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = JobModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                return redirect("/job/")
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)


# =========================== DELETE VIEW =========================== #
class JobDeleteView(JobObjectMixinView, View):
    template_name = 'job/job_delete.html'

    #  GET METHOD
    def get(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)

    # POST METHOD
    def post(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect("/job/")
        return render(request, self.template_name, context)

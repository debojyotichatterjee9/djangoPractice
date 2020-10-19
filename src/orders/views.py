from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
# 
from .forms import OrderModelForm
from .models import Order 
# # BASE VIEW CLass = VIEW
# 
class OrderObjectMixin(object):
    model = Order
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id=id)
        return obj
# 
# class OrderDeleteView(OrderObjectMixin, View):
#     template_name = "orders/orders_delete.html" # DetailView
#     def get(self, request, id=None, *args, **kwargs):
#         # GET method
#         context = {}
#         obj = self.get_object()
#         if obj is not None:
#             context['object'] = obj
#         return render(request, self.template_name, context)
# 
#     def post(self, request, id=None,  *args, **kwargs):
#         # POST method
#         context = {}
#         obj = self.get_object()
#         if obj is not None:
#             obj.delete()
#             context['object'] = None
#             return redirect('../list')
#         return render(request, self.template_name, context)
# 
# 
class OrderUpdateView(OrderObjectMixin, View):
    template_name = "orders/orders_update.html" # DetailView
    def get_object(self):
        id = self.kwargs.get('order_id')
        obj = None
        if id is not None:
            obj = get_object_or_404(Order, id=id)
        return obj

    def get(self, request, id=None, *args, **kwargs):
        # GET method
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = OrderModelForm(instance=obj)
            context['order'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request, id=None,  *args, **kwargs):
        # POST method
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = OrderModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            else:
                print("Form error")
            context['order'] = obj
            context['form'] = form
        return render(request, self.template_name, context)
# 
# 
class OrderCreateView(View):
    template_name = "orders/orders_create.html" # DetailView
    def get(self, request, *args, **kwargs):
        # GET method
        form = OrderModelForm()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # POST method
        form = OrderModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = OrderModelForm()
        context = {"form": form}
        return render(request, self.template_name, context)
# 
# 
class OrderDetailView(View):
    template_name = "orders/orders_detail.html"
    queryset = Order.objects.all()

    def get_object(self):
        id = self.kwargs.get('order_id')
        obj = None
        if id is not None:
            obj = get_object_or_404(Order, id=id)
        return obj

    def get(self, request, id=None, *args, **kwargs):
      # GET method
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = OrderModelForm(instance=obj)
            context['order'] = obj
            context['form'] = form
        return render(request, self.template_name, context)
    
    
class OrderListView(View):
    template_name = "orders/orders_list.html"
    queryset = Order.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {'orders_list': self.get_queryset()}
        return render(request, self.template_name, context)


class OrderView(OrderObjectMixin, View):
    template_name = "orders/orders_detail.html" # DetailView
    def get(self, request, id=None, *args, **kwargs):
        # GET method
        context = {'order': self.get_object()}
        print(context)
        return render(request, self.template_name, context)

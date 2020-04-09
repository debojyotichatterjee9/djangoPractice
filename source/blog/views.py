from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
from .models import Article
from .forms import ArticleModelForm


# ========================== LIST VIEW ========================== #
class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all() #<blog>/<modelname>/_<generic view name> -  this is how Django looks for a template for class based view function


# ========================== DETAIL VIEW ========================== #
class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'
    # queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id = id_)


# ========================== CREATE VIEW ========================== #
class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm # to get the model form
    queryset = Article.objects.all()
    # we can change the url where we want to redirect after the article is saved or we can create a function as mentioned below
    # success_url = '/blog'
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    # we can change the url where we want to redirect after the article is saved by a function as mentioned below
    # def get_success_url(self):
    #     return '/blog'


# ========================== UPDATE VIEW ========================== #
class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_create.html' # we can use the same html view file as used in create. it will be the same.
    form_class = ArticleModelForm # to get the model form
    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id = id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

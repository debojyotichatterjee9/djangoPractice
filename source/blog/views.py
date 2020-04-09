from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
from .models import Article
from .foorms import ArticleModelForm

class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all() #<blog>/<modelname>/_<generic view name> -  this is how Django looks for a template for class based view function

class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'
    # queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id = id_)

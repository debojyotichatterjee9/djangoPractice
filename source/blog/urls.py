from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView
)

app_name = 'blog'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    
]

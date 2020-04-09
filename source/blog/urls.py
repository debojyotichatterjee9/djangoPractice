from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
)

app_name = 'blog'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),

    # by default django looks for a pk(primary key) or a slug as param
    # path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail')
    # below is another way to do it
    path('<int:id>/', ArticleDetailView.as_view(), name='article_detail'),
    path('create/', ArticleCreateView.as_view(), name='article_create'),
    path('<int:id>/update/', ArticleUpdateView.as_view(), name='article_update'),
    path('<int:id>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
]

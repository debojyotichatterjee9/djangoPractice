from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView
)

app_name = 'blog'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),

    # by default django looks for a pk(primary key) or a slug as param
    # path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail')
    # below is another way to do it
    path('<int:id>/', ArticleDetailView.as_view(), name='article_detail')
]

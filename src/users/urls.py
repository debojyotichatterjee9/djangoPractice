from django.urls import path
from .views import user_detail_view
from .views import (
    UserListView
)

app_name="users"
urlpatterns = [
    # path('list', user_list_view, name='list'),
    path('list', UserListView.as_view(), name='list'),
    path('details/<str:user_id>', user_detail_view, name='details'),
    ]

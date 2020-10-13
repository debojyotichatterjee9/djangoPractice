from django.urls import path
# we are using class based view so these are not reqd
# from .views import user_list_view, user_detail_view
from .views import (
    UserCreateView,
    UserListView,
    UserDetailView,
    UserUpdateView,
    UserDeleteView
)

app_name="users"
urlpatterns = [
    # path('list', user_list_view, name='list'),
    path('create', UserCreateView.as_view(), name='create'),
    path('list', UserListView.as_view(), name='list'),
    path('details/<str:user_id>', UserDetailView.as_view(), name='details'), #class based view searches with the keyword pk but we are overriding it
    path('update/<str:user_id>', UserUpdateView.as_view(), name='update'),
    path('delete/<str:user_id>', UserDeleteView.as_view(), name='delete'),
    ]

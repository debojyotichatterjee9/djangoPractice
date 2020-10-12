from django.urls import path
from .views import user_list_view, user_detail_view

app_name="users"
urlpatterns = [
    path('list', user_list_view, name='list'),
    path('details/<str:user_id>', user_detail_view, name='details'),
    ]

from django.urls import path
from .views import (
    JobView,
    JobListView,
    JobCreateView,
    JobUpdateView,
    JobDeleteView
    # my_fbv
)

app_name = 'job'
urlpatterns = [
    path('', JobListView.as_view(), name='jobs_list'),
    # path('', my_fbv, name='Jobs-list'),


    path('create/', JobCreateView.as_view(), name='jobs_create'),
    path('<int:id>/', JobView.as_view(), name='jobs_detail'),
    path('<int:id>/update/', JobUpdateView.as_view(), name='jobs_update'),
    path('<int:id>/delete/', JobDeleteView.as_view(), name='jobs_delete'),

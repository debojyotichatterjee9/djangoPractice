from django.urls import path
from .views import (
    # OrderView,
    OrderListView,
    # OrderCreateView,
    # OrderUpdateView,
    # OrderDeleteView
)

app_name = 'orders'
urlpatterns = [
    # path('create', OrderCreateView.as_view(), name='create'),
    path('list', OrderListView.as_view(), name='list'),
    # path('order/<order_id>', OrderView.as_view(), name='detail'),
    # path('update/<order_id>', OrderUpdateView.as_view(), name='update'),
    # path('delete/<order_id>', OrderDeleteView.as_view(), name='delete'),
]
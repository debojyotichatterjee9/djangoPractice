from django.urls import path
from .views import product_create_view, product_list_view, product_detail_view, product_update_view, product_delete_view

app_name="products"
urlpatterns = [
    path('create', product_create_view, name='create'),
    path('list', product_list_view, name='list'),
    path('details/<str:product_id>', product_detail_view, name='details'),
    path('update/<product_id>', product_update_view, name='update'),
    path('delete/<product_id>', product_delete_view, name='delete'),
]

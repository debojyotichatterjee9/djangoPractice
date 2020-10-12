from django.urls import path
from .views import product_detail_view, product_create_view, product_delete_view, product_list_view, product_update_view

app_name="products"
urlpatterns = [
    path('details/<str:product_id>', product_detail_view, name='details'),
    path('create', product_create_view, name='create'),
    path('delete/<product_id>', product_delete_view, name='delete'),
    path('list', product_list_view, name='list'),
    path('update/<product_id>', product_update_view, name='update'),
]

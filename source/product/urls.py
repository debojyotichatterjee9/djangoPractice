from django.urls import path
from .views import (
    product_detail_view,
    product_create_view,
    product_create_view_two,
    product_create_view_three,
    product_update_view,
    product_delete_view,
    product_list_view,
    google_search_view
)

app_name = 'product'
urlpatterns = [
    path('create/', product_create_view, name="create"),
    path('<int:pid>/', product_detail_view, name="product_detail"),
    path('create_two/', product_create_view_two, name="create_two"),
    path('create_three/', product_create_view_three, name="create_three"),
    path('update/<int:pid>/', product_update_view, name="product_update"),
    path('<int:pid>/delete/', product_delete_view, name="product_delete"),
    path('productList/', product_list_view, name="product_list"),
    path('google_search/', google_search_view, name="google_search")
]

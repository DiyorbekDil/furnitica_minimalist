from django.urls import path
from products import views


app_name = 'products'

urlpatterns = [
    path('list/', views.ProductListView.as_view(), name='product_list'),
    path('detail/', views.ProductDetailView.as_view(), name='product_detail'),
]

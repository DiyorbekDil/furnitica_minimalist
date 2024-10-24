from django.urls import path
from ordering import views


app_name = 'ordering'

urlpatterns = [
    path('cart/', views.UserCartView.as_view(), name='cart'),
    path('checkout/', views.OrderCreateView.as_view(), name='checkout'),
    path('user-wishlist/', views.UserWishlistView.as_view(), name='user_wishlist'),
    path('cart/<int:pk>/', views.add_or_remove, name='add-or-remove'),
]
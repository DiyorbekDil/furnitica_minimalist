from django.urls import path
from ordering import views


app_name = 'ordering'

urlpatterns = [
    path('cart/', views.ProductCartView.as_view(), name='cart'),
    path('checkout/', views.ProductCheckoutView.as_view(), name='checkout'),
    path('user-wishlist/', views.UserWishlistView.as_view(), name='user_wishlist'),
]
from django.urls import path
from users import views


app_name = 'users'

urlpatterns = [
    path('user/register', views.UserRegisterView.as_view(), name='register'),
    path('user/login', views.UserLoginView.as_view(), name='login'),
    path('user/account', views.UserAccountView.as_view(), name='account'),
    path('user/reset', views.UserResetView.as_view(), name='reset'),
    path('user/wishlist', views.UserWishlistView.as_view(), name='wishlist'),
]
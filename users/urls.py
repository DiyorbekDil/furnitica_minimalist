from django.urls import path
from users import views


app_name = 'users'

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('account/', views.UserAccountView.as_view(), name='account'),
    path('reset/', views.UserResetView.as_view(), name='reset'),
]
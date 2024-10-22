from django.urls import path

from pages import views

app_name = 'pages'

urlpatterns = [
    path('contact/', views.ContactCreateView.as_view(), name='contact'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('404/', views.View404.as_view(), name='404'),
    path('', views.HomePageView.as_view(), name='home'),
]
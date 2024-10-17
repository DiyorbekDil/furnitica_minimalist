from django.urls import path
from blogs import views


app_name = 'blogs'

urlpatterns = [
    path('detail/', views.BlogDetailView.as_view(), name='detail'),
    path('list/', views.BlogListView.as_view(), name='list'),
]
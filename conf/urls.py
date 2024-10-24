from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from conf import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ordering/', include('ordering.urls', namespace='ordering')),
    path('products/', include('products.urls', namespace='products')),
    path('users/', include('users.urls', namespace='users')),
    path('blogs/', include('blogs.urls', namespace='blogs')),
    path('', include('pages.urls', namespace='pages')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'conf.views.handler404'
# handler500 = 'conf.views.handler500'
# handler401 = 'conf.views.handler401'
# handler043 = 'conf.views.handler403'

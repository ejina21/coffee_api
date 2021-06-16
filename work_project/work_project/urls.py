from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/base_auth/', include('rest_framework.urls')),
    path('api/v1/coffee/', include('coffee.urls')),
]

urlpatterns += doc_urls

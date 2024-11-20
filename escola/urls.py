from django.contrib import admin
from django.urls import path , include
from rest_framework import serializers


urlpatterns = [
    path('api/v1/', include('curso.urls')),
    path('admin/', admin.site.urls),
    path('auth/',include('rest_framework.urls'))
]

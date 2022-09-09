from django.contrib import admin
from django.urls import path, include
from proyecto_Raiz import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.main.urls')),
    path('', include('apps.reserva.urls')),
]
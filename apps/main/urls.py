from django.contrib import admin
from django.urls import path, include

from apps.main.views import mainTemplateView

urlpatterns = [
    path('', mainTemplateView.as_view(),name='inicio'),
    path('activos/', include('apps.Activos.urls')),
]
from django.shortcuts import render
from django.views.generic.base import TemplateView


class mainTemplateView(TemplateView):
    template_name = "main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Radiator Springs"
        context['titulo_header'] = "Bienvenido"
        context['url_anterior'] = '/'
        return context
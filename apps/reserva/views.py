from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView

from apps.reserva.models import Reserva
from .forms import ReservaForm

class ReservaListView(ListView):
    template_name = "Reserva/listarReserva.html"
    context_object_name = 'reserva'
    model = Reserva

    def get_queryset(self):
        query = self.request.GET.get("query")
        print(query)
        if query:
            return self.model.objects.filter(nombres__icontains=query)
        else:
            return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_anterior'] = '/'
        context['crear_url'] = '/Reserva/crearReserva'
        context['editar_url'] = '/Reserva/editarReserva'
        context['titulo'] = 'Reservas | Radiator Springs'
        context['titulo_header'] = 'Listado de Reservas'
        context['titulo_tabla'] = 'Reservas'
        context['query'] = self.request.GET.get("query") or ""
        return context


class CrearReserva(CreateView):
    model = Reserva
    template_name = "Reserva/crearReserva.html"
    success_url = reverse_lazy('reserva:listarReserva')
    form_class = ReservaForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Solicitud de Reserva | Radiator Springs'
        # context['action_save'] = '/reservar/'
        context['titulo_header'] = 'Formulario de Reserva'
        # context['listar_url'] = '/reservar/'
        context['url_anterior'] = '/'
        context['action'] = 'add'
        return context

# class ActualizarReserva(UpdateView):
#     model = Reserva
#     template_name = "Reserva/crearReserva.html"
#     success_url = reverse_lazy('reserva:listarReserva')
#     form_class = ReservaForm
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['action_save'] = self.request.path
#         context['titulo'] = 'Solicitud de Reserva | Radiator Springs'
#         context['titulo_header'] = 'Edición de Reserva'
#         # context['listar_url'] = '/reservar/'
#         context['url_anterior'] = '/'
#         # context['action'] = 'add'
#         return context
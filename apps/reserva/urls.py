from django.urls import path
from apps.reserva.views import ReservaListView, CrearReserva

app_name = "reserva"
urlpatterns = [
    path('reservar/', ReservaListView.as_view(), name='listarReserva'),
    path('generar/', CrearReserva.as_view(), name='crearReserva'),
    # path('actualizar/<int:pk>/', ActualizarReserva.as_view(), name='editReserva'),
]

from django.urls import path
from apps.Activos.views.producto.views import ProductoListView

app_name = "activo"
urlpatterns = [
    path('productos/', ProductoListView.as_view(), name='listarProducto'),
]
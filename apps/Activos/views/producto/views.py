from django.shortcuts import render
from django.views.generic import ListView
from apps.Activos.models import Producto

class ProductoListView(ListView):
    template_name = "Activos/Producto/listarProducto.html"
    context_object_name = 'producto'
    model = Producto

    def get_queryset(self):
        query = self.request.GET.get("query")

        if query:
            return self.model.objects.filter(nombres__icontains=query)
        else:
            return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_anterior'] = '/'
        context['titulo'] = 'Listado de Productos | Radiator Springs'
        context['titulo_header'] = 'Productos'
        context['query'] = self.request.GET.get("query") or ""

        return context

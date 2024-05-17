from typing import Any
from django.views.generic.base import TemplateView
from django.db.models import Q

from alumno.models import Alumno


class HomePage(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        condicion = Q(nombre__icontains=self.request.GET.get("nombre")) | Q(
            apellido__icontains=self.request.GET.get("apellido")
        )
        context["alumnos"] = (
            Alumno.objects.filter(condicion)
            if self.request.GET.get("nombre")
            else Alumno.objects.all()
        )

        # En el filter ponemos los atributos que queremos agregar
        # Alumno.objects.filter

        # En el exclude ponemos los atributos que queremos sacar
        # Alumno.objects.exclude

        # AND en django
        # Alumno.objects.filter(
        # nombre__icontais="Juan", apellido__icontains="Perez")
        # )

        # OR en django
        # Se usa con el Q y el |

        # Alumno.objects.filter(Q(condicion=1) | Q(condicion=2))

        return context


"""
calendario -> eventos de 10 a 22 cada 20 minutos / 12 * 3 = 36
recurso:
nuestra_app/calendario/
nuestra_app/calendario/{id}/?peluquero=[id]
nuestra_app/calendario/{id}/editar
nuestra_app/calendario/fecha/{fecha}/


API:
    nuestra_app/calendario/{id}/ PUT
    nuestra_app/calendario/{id}/ PATCH
    nuestra_app/calendario/{id}/ DELETE
    nuestra_app/calendario/ POST
    nuestra_app/calendario/ GET


nuestra_app/turno/registrar/
nuestra_app/turno/?fecha_desde=[fecha]&fecha_hasta=[fecha]
nuestra_app/turno/{id}/
nuestra_app/turno/{id}/editar/
nuestra_app/turno/{peluquero_id}?fecha_desde=[fecha]&fecha_hasta=[fecha]


nuestra_app/peluquero/ -> listado de peluqueros
nuestra_app/peluquero/{id}/ -> detalle de peluquero
nuestra_app/peluquero/{id}/calendario/{id}/?fecha=[fecha] -> calendario de peluquero
nuestra_app/peluquero/{id}/calendario/{id}/turno/{id}/ -> detalle de turno


{valor} -> variables de url
[fecha] -> parametros dentro url

transaccion atomica django
importamos transaction de django.db

from django.db import transaction
with transaction.atomic():
    # codigo a ejecutar
    pass

UUID -> identificador unico universal
ejemplo:
    123e4567-e89b-12d3-a456-426614174000
"""

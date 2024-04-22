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

from django.contrib import admin

from alumno.models import Alumno


@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "dni", "carrera")
    search_fields = ("nombre", "apellido", "dni")
    list_filter = ("carrera",)

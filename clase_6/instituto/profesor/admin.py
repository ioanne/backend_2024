from django.contrib import admin

from profesor.models import Profesor


@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "dni")
    search_fields = ("nombre", "apellido", "dni")
    list_filter = ("materia",)

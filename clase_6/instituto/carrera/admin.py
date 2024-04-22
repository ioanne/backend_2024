from django.contrib import admin

from carrera.models import Carrera


@admin.register(Carrera)
class CarreraAdmin(admin.ModelAdmin):
    list_display = ("nombre", "duracion")
    search_fields = ("nombre",)
    filter_horizontal = ("materia",)

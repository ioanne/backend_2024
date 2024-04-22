from django.contrib import admin

from materia.models import Materia


@admin.register(Materia)
class Materia(admin.ModelAdmin):
    list_display = ("nombre", "duracion")
    search_fields = ("nombre",)

from django.db import models

from custom_user.models import PersonaAbstract


class Peluquero(PersonaAbstract):

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"

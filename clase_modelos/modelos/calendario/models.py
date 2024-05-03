from django.db import models

from turno.models import Turno


class Calendario(models.Model):
    peluquero = models.ForeignKey("peluquero.Peluquero", on_delete=models.CASCADE)

    @staticmethod
    def validar_bloque_horario(peluquero_id, servicio_id, fecha, hora):
        # Hacemos la validacion para saber si podemos crear o no el turno
        # Turnos del peluquero
        pass

    def __str__(self) -> str:
        return f"{self.fecha} {self.hora}"

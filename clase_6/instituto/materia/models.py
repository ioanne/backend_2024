from django.db import models


class Materia(models.Model):
    nombre = models.CharField(max_length=50)
    duracion = models.IntegerField()
    descripcion = models.TextField()

    def __str__(self) -> str:
        return self.nombre

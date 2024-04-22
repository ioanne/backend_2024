from django.db import models


class Carrera(models.Model):
    nombre = models.CharField(max_length=50)
    duracion = models.IntegerField()
    descripcion = models.TextField()
    materia = models.ManyToManyField("materia.Materia", null=True, blank=True)

    def __str__(self) -> str:
        return self.nombre

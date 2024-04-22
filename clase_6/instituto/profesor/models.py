from django.db import models


class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.CharField(max_length=8)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    materia = models.ManyToManyField("materia.Materia")

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"

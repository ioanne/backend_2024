from django.db import models

from django.contrib.auth.models import AbstractUser


class PersonaAbstract(models.Model):
    class Meta:
        abstract = True

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)


class CustomUser(AbstractUser):
    pass

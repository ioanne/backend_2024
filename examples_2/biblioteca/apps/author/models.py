from django.db import models


class Author(models.Model):
    """Los modelos de django crean tablas y celdas en una base datos relacional"""
    name = models.CharField(max_length=255)
    pais = models.CharField(max_length=80)
    email = models.EmailField()
    nacimiento = models.DateField()
    altura = models.IntegerField()

    def __str__(self):
        return f'name: {self.name} pais: {self.pais}, email: {self.email}'

# PEP-8 PEP-256
# BookAuthor Upper Camelcase (clases)
# get_author() snake case (funciones)
# valor_dato snake case (variables)
# _valor_dato snake case (variable privada)
# __valor_dato snake case (variable MUY privada) (no se usa casi nunca a no ser que hagamos una libreria)
# archivo.py snake case (modulos)



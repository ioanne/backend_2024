from django.db import models


class Turno(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    calendario = models.ForeignKey("calendario.Calendario", on_delete=models.CASCADE)
    servicio = models.ForeignKey("servicio.Servicio", on_delete=models.CASCADE)
    cliente = models.ForeignKey("cliente.Client", on_delete=models.CASCADE)

    @staticmethod
    def bloque_valido(fecha, hora, servicio_id):
        """Pre condiciones:
        Validar que el bloque este dentro del rango permitido dependiendo el servicio
        Dentro del horario
        el bloque tiene que ser de X minutos dependiendo el servicio
        Devuelve True o False


        EJ Fecha:
            Tiene que ser un dia que se brinde el servicio.
            Si el servicio se da lunes y miercoles
            Solo puede ser entre esos 2 días.

        EJ:
            Si es de media hora:
                10:00 - 10:30
                10:30 - 11:00
                11:00 - 11:30
                11:30 - 12:00
                ETC
        """


"""
MVT

Modelo
    Todo lo relacionado al acceso a base de datos

Vista
    Lógica de negocio
    Donde vamos a utilizar todo lo creamos en el modelo


Template
    Sistema de template HTML de django
"""


"""
MVC
Modelo
Vista
Controlador

"""

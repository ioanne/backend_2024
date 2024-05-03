from django.db import models


class Turno(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    calendario = models.ForeignKey("calendario.Calendario", on_delete=models.CASCADE)
    servicio = models.ForeignKey("servicio.Servicio", on_delete=models.CASCADE)
    cliente = models.ForeignKey("cliente.Client", on_delete=models.CASCADE)

    # models.OneToOneField("calendario.Calendario", on_delete=models.CASCADE)
    # models.ManyToManyField("peluquero.Peluquero")

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
En la documentación de Django, puedes encontrar detalles sobre los tipos de relaciones que puedes establecer entre modelos. Aquí te resumo las principales:

Relaciones uno a uno (One-to-one): Utiliza OneToOneField para definir una relación uno a uno.
Por ejemplo, si tienes un modelo Place y un modelo Restaurant,
cada Place puede estar asociado a un solo Restaurant y viceversa​ https://docs.djangoproject.com/en/5.0/topics/db/examples/one_to_one/

Relaciones uno a muchos (Many-to-one): Usa ForeignKey para este tipo de relación.
Un ejemplo sería un modelo Reporter que puede tener asociados muchos Article,
pero cada Article solo está asociado a un Reporter​ https://docs.djangoproject.com/en/5.0/topics/db/examples/many_to_one/​.

Relaciones muchos a muchos (Many-to-many): Se define con ManyToManyField.
Por ejemplo, un modelo Article puede estar asociado con muchos Publication y
cada Publication puede tener muchos Article.
Además, puedes agregar y quitar objetos de estas relaciones
sin necesidad de guardar cada instancia,
facilitando la manipulación de las relaciones​ https://docs.djangoproject.com/en/5.0/topics/db/examples/many_to_many/​.
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

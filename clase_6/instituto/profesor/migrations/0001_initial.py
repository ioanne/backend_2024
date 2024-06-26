# Generated by Django 5.0.4 on 2024-04-19 22:31

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("materia", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profesor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=50)),
                ("apellido", models.CharField(max_length=50)),
                ("dni", models.CharField(max_length=8)),
                ("fecha_nacimiento", models.DateField()),
                ("direccion", models.CharField(max_length=100)),
                ("telefono", models.CharField(max_length=15)),
                ("email", models.EmailField(max_length=254)),
                ("materia", models.ManyToManyField(to="materia.materia")),
            ],
        ),
    ]

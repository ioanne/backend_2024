# Generated by Django 5.0.4 on 2024-05-17 22:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("book", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="is_published",
            field=models.BooleanField(default=False),
        ),
    ]
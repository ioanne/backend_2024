from django.db import models


class BookManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(is_published=True)


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13)
    pages = models.IntegerField()
    is_published = models.BooleanField(default=True)


    objects = BookManager()
    objects_all = models.Manager()

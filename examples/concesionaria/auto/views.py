from django.shortcuts import render
from django.http import HttpResponse


def vista_auto(request):
   return HttpResponse("¡Hola, esta es mi primera aplicación creada en la clase de Backend!")

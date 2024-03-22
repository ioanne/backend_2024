# Creación de un nuevo proyecto Django

## 1. Crear el entorno virtual
```bash
python -m venv env
```

## 2. Activar Entorno Virtual
Activa el entorno virtual:



```bash
# En windows:
Env\Scripts\activate
```


```bash
## En Unix o macOS:
source Env/bin/activate
```


## 3. Instalar Django
Instala Django dentro del entorno virtual:

```bash
pip install django
```


## 4. Crear requirements.txt
Crea un archivo `requirements.txt` que contenga las dependencias del proyecto:
```bash
pip freeze > requirements.txt
```

## 5. Crear nuevo proyecto
Crea un nuevo proyecto de Django:
```bash
django-admin startproject [nombreproyecto]
```
Reemplaza `nombreproyecto` con el nombre que desees darle a proyecto.


## 6. Correr servidor de desarrollo
Entra en el directorio del proyecto y corre el servidor de desarrollo:
```bash
cd nombreproyecto
python manage.py runserver
```

Una vez que hayas completado estos pasos, podrás acceder al sitio predeterminado de Django en `http://127.0.0.1:8000/`.



# Crear una nueva app
Para crear una nueva app en tu proyecto de Django, sigue estos pasos:

## 1. Entra al directorio del proyecto
Asegúrate de estar en el directorio raíz de tu proyecto de Django:

```bash
cd nombreproyecto
```

## 2. Crea una nueva app
Utiliza el comando `startapp` de Django para crear una nueva app:

```bash
python manage.py startapp [nombreapp]
```
Reemplaza `nombreapp` con el nombre que desees darle a tu nueva app.


## 3. Registra la app
Abre el archivo `settings.py` ubicado en el directorio raíz del proyecto y busca la sección `INSTALLED_APPS`. Agrega el nombre de tu nueva app a esta lista:

```python
INSTALLED_APPS = [
    # ...
    'nombreapp',
]
```

# Crear modelos
## 1. Crear un nuevo modelo
Dentro del directorio de tu app, abre el archivo `models.py`. Este archivo es donde definirás tus modelos.

## 2. Importa modelos de Django
En la parte superior del archivo, importa los modelos necesarios de Django:
```python
from django.db import models
```

## 3. Crea una nueva clase de modelo
Crea una nueva clase de modelo que herede de models.Model. Esta clase representará una tabla en tu base de datos.
```python
class NombreModelo(models.Model):
    # Campos del modelo
    pass
```
Reemplaza NombreModelo con el nombre que desees darle a tu modelo.

## 4. Agrega campos al modelo
Dentro de la clase NombreModelo, define los campos que conformarán tu modelo. Cada campo es una instancia de un tipo de campo específico.
```python
class NombreModelo(models.Model):
    nombre_campo_1 = models.CharField(max_length=100)
    nombre_campo_2 = models.IntegerField()
    nombre_campo_3 = models.DateField()
    # ... más campos
```

Django proporciona varios tipos de campos, como CharField, IntegerField, DateField, ForeignKey, entre otros. Puedes personalizar estos campos con opciones adicionales, como max_length, default, null, etc.

## 5. Agrega métodos y metadatos (opcional)
Puedes agregar métodos y metadatos a tu modelo según tus necesidades.


```python
class NombreModelo(models.Model):
    nombre_campo_1 = models.CharField(max_length=100)
    nombre_campo_2 = models.IntegerField()
    nombre_campo_3 = models.DateField()
    # ... más campos

    def __str__(self):
        return self.nombre_campo_1

    class Meta:
        verbose_name_plural = "Nombre plural del modelo"
```
El método __str__ define cómo se representará el objeto del modelo como una cadena de texto. La clase Meta te permite configurar opciones adicionales para tu modelo.



## 6. Migra los cambios al modelo
Si has creado nuevos modelos en models.py, necesitarás realizar las migraciones correspondientes:

```bash
python manage.py makemigrations
python manage.py migrate
```


# Crear una Nueva Vista y Configurar urls.py
## 1. Crear una nueva vista

Abre el archivo `views.py` dentro del directorio de tu app y crea una nueva función que represente tu vista:

```python
# views.py
from django.shortcuts import render
from django.http import HttpResponse

def nombre_vista(request):
   # Lógica de la vista
   return HttpResponse("¡Hola, esta es mi primera aplicación creada en la clase de Backend!")
```

En este ejemplo, hemos creado una función llamada nombre_vista que recibe el objeto request como argumento. Por ahora, simplemente retorna un HttpResponse con un mensaje.

## 2. Configurar urls.py de la App
Crea el archivo urls.py dentro del directorio de tu app y agrega una nueva ruta asociada a tu vista:

```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('ruta/', views.nombre_vista, name='nombre_ruta'),
]
```

Aquí, hemos definido una nueva ruta ruta/ que apunta a la vista nombre_vista. Además, hemos asignado un nombre nombre_ruta a esta ruta para poder hacer referencia a ella más adelante.

## 3. Configurar urls.py del Proyecto
Finalmente, necesitamos incluir las urls de nuestra app en el archivo urls.py del proyecto. Abre el archivo urls.py en el directorio raíz del proyecto y agrega la siguiente línea:

```python
# urls.py (proyecto)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('nombreapp.urls')),
]
```

Aquí, hemos incluido las urls de nuestra app nombreapp en las urls del proyecto. La ruta vacía '' indica que todas las rutas definidas en nombreapp.urls se incluirán en la raíz del sitio.

## 4. Acceder a la Vista
Ahora, cuando accedas a http://localhost:8000/ruta/ en tu navegador, deberías ver el mensaje "¡Hola, esta es mi primera aplicación creada en la clase de Backend!".

Puedes continuar agregando más vistas y urls según tus necesidades. Recuerda reemplazar nombreapp con el nombre real de tu app en el proyecto.
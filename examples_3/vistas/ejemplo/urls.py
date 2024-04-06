from django.urls import path
from ejemplo.views import ejemplo, Vista

urlpatterns = [
    # Funcion que mapea una vista con una URL
    path('ejemplo/', ejemplo, name='ejemplo'),
    path('ejemplo2/', Vista.as_view(), name='ejemplo2'),
]
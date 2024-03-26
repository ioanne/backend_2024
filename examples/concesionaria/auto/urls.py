from django.urls import path
from auto.views import vista_auto

urlpatterns = [
    path('vista/', vista_auto, name='vista_auto'),
]
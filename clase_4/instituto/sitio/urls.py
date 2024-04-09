from django.urls import path

from sitio.views import Home

urlpatterns = [
    path('home/', Home.as_view(), name='home'),
    
]
from django.urls import path
from sitio.views import HomePage

urlpatterns = [
    path("", HomePage.as_view(), name="home"),
]

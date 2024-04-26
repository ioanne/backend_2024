from django.urls import path

from dashboard.views import DashboardTemplateView

urlpatterns = [
    path("", DashboardTemplateView.as_view(), name="index"),
]

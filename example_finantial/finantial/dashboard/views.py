from django.shortcuts import render
from django.views.generic.base import TemplateView


class DashboardTemplateView(TemplateView):
    template_name = "index.html"

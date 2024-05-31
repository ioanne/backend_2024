from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.views.generic import View
from django.urls import reverse_lazy

from custom_user.forms import RegistrationForm


class CustomLoginView(LoginView):
    template_name = "login.html"

    def form_invalid(self, form):
        messages.error(
            self.request, "Credenciales incorrectas. Por favor, inténtalo de nuevo."
        )  # Mensaje de error
        return super().form_invalid(form)


class CustomLogoutView(LogoutView):
    pass


class LogoutConfirmationView(View):
    template_name = "logout.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class RegistrationView(CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy("login")
    template_name = "register.html"

    def form_valid(self, form):
        # Procesar el formulario si es válido
        user = form.save(commit=False)
        user.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        # Agregar mensajes de error a la lista de mensajes
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{field}: {error}")
        return super().form_invalid(form)

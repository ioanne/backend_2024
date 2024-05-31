from django import forms

from custom_user.models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        help_text="Required. Inform a valid email address.",
    )

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2")

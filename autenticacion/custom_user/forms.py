from django import forms

from custom_user.models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    """
    Esta clase hereda de UserCreationForm
    UserCreationForm contiene usernamme, password1 y password2
    Se le agrega email

    """
    email = forms.EmailField(
        max_length=254,
        help_text="Required. Inform a valid email address.",
    )

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2")

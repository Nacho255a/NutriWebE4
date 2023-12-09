from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class RegistroUsuarioForm(UserCreationForm):
    username = forms.CharField(
        max_length=9,
        label="Rut",
        validators=[
            RegexValidator(
                regex=r"^\d{1,9}",
                message="El RUT de 8 a 9 dígitos",
                code="invalid_rut",
            )
        ],
        widget=forms.TextInput(attrs={"type": "number"}),
        help_text="Requerido. Ingrese su RUT sin puntos ni guión. Por ejemplo: 123456789.",
    )
    first_name = forms.CharField(
        max_length=30,
        label="Nombre",
        required=True,
        help_text="Requerido. Máximo 30 caracteres.",
    )
    last_name = forms.CharField(
        max_length=30,
        label="Apellido",
        required=True,
        help_text="Requerido. Máximo 30 caracteres.",
    )
    email = forms.EmailField(
        max_length=254,
        required=True,
        help_text="Requerido. Ingrese una dirección de correo electrónico válida.",
    )

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )

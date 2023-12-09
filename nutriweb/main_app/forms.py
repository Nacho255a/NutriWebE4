from django import forms
from .models import Citas
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class RegistroUsuarioForm(UserCreationForm):
    username = forms.CharField(
        max_length=9,
        label="Rut",
        validators=[
            RegexValidator(
                regex=r"^\d{8,9}",
                message="El RUT de 8 a 9 dígitos",
                code="invalid_rut",
            )
        ],
        widget=forms.TextInput(attrs={"type": "number"}),
        help_text="Ingrese su RUT sin puntos ni guión. Por ejemplo: 123456789.",
    )
    first_name = forms.CharField(
        max_length=30,
        label="Nombre",
        required=True,
        help_text="Máximo 30 caracteres.",
    )
    last_name = forms.CharField(
        max_length=30,
        label="Apellido",
        required=True,
        help_text="Máximo 30 caracteres.",
    )
    email = forms.EmailField(
        max_length=254,
        required=True,
        help_text="Ingrese una dirección de correo electrónico válida.",
    )
    password1 = forms.CharField(
        label="Contraseña", # Cambia el label a 'Contraseña'
        max_length=254,
        required=True,
        help_text="Máximo 254 caracteres.",
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label="Confirmar contraseña", # Cambia el label a 'Confirmar contraseña'
        max_length=254,
        required=True,
        widget=forms.PasswordInput,
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

class ProgramarCitaForm(forms.ModelForm):
    class Meta:
        model = Citas
        fields = ['RutCliente', 'RutNutricionista', 'FechaCita', 'HoraCita', 'LugarCita']

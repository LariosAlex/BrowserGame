from .models import User
from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].validators = []

        # Optionally, you can also remove the help text for the password field:
        self.fields['password1'].help_text = ''

    username = forms.CharField(
        label=_("Nombre de Usuario:"),
        help_text=_("Debe de tener como mucho 25 caracteres se aceptan solo letras, digitos y estos caracteres especiales: @/./+/-/_"),
        max_length=25,
        widget=forms.TextInput(attrs={'autofocus': True}),
    )
    email = forms.EmailField(
        label=_("Correo Electrónico:"),
        help_text=_("Introduce tu correo electrónico"),
        max_length=254,
        widget=forms.EmailInput(),
    )
    password1 = forms.CharField(
        label=_("Contraseña:"),
        help_text=_(""),
        max_length=30,
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    password2 = forms.CharField(
        label=_("Repite la contraseña:"),
        max_length=30,
        strip=False,
        help_text=_("Debe ser identica a la contraseña!"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
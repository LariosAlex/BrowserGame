from .models import User
from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].validators = []

        # Opcionalment, també es pot eliminar el text d'ajuda per al camp de la contrasenya:
        self.fields['password1'].help_text = ''

    username = forms.CharField(
        label=_("Nom d'usuari:"),
        help_text=_("Ha de tenir com a màxim 25 caràcters i només s'accepten lletres, dígits i aquests caràcters especials: @/./+/-/_"),
        max_length=25,
        widget=forms.TextInput(attrs={'autofocus': True}),
    )
    email = forms.EmailField(
        label=_("Correu electrònic:"),
        help_text=_("Introdueix el teu correu electrònic"),
        max_length=254,
        widget=forms.EmailInput(),
    )
    password1 = forms.CharField(
        label=_("Contrasenya:"),
        help_text=_(""),
        max_length=30,
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    password2 = forms.CharField(
        label=_("Repeteix la contrasenya:"),
        max_length=30,
        strip=False,
        help_text=_("Ha de ser idèntica a la contrasenya!"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

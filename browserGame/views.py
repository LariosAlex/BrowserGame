from .forms import *
from django.shortcuts import render, redirect
from django.contrib.auth.forms import *
from django.contrib.auth import login
from django.utils.translation import gettext_lazy as _


# Create your views here.
def index(request):
    context = {}

    return render(request, 'browserGame/index.html', context)


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redireccionar a la página de inicio después de iniciar sesión exitosamente
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})



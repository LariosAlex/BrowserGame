from .forms import *
from django.shortcuts import render, redirect
from django.contrib.auth.forms import *
from django.contrib.auth import login
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import PasswordResetForm
from .models import *
from django.http import HttpRequest
from django.core.exceptions import *
from django.utils import timezone
from .utils import save_log
from django.core.mail import send_mail
from django.conf import settings

def vue(request):
    context = {}

    return render(request, 'browserGame/index.html', context)


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('landing')
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
            return redirect('landing')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def password_reset_done(request):
    return render(request, 'browserGame/password_reset_done.html')

def password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(request=request)
    else:
        form = PasswordResetForm()
    context = {'form': form}
    return render(request, 'browserGame/password_reset_form.html', context)

def landing(request):
    active_season = Season.objects.latest("id")
    save_log('SQL', 'Season.objects.latest("id")', request)
    save_log('SQL', str(Season.objects.latest("id")), request)
    actions = None
    characters = Character.objects.filter(season=active_season).order_by('-level', '-exp')
    save_log('SQL', "Character.objects.filter(season=active_season).order_by('-level', '-exp')", request)
    save_log('SQL', str(characters), request)
    save_log('INF', 'Accediendo a vista', request)
    if request.user.is_authenticated:
        try:
            character = Character.objects.get(season=active_season, user=request.user)
            actions = ActionLog.objects.filter(performer=character)
        except ObjectDoesNotExist:
            character = None
    else:
        character = None
    context = {
        'season': active_season,
        'character' : character,
        'actions' : actions,
        'characters': characters
    }
    return render(request, 'browserGame/landing.html', context)

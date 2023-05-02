from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.http import HttpRequest
from django.core.exceptions import *
from django.utils import timezone
from .utils import save_log

def vue(request):
    context = {}

    return render(request, 'browserGame/index.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('landing')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
    
def landing(request):
    active_season = Season.objects.get(id=1)
    save_log('INF', 'SQL-'+str(active_season), request)
    actions = None
    characters = Character.objects.filter(season=active_season).order_by('-level', '-exp')
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

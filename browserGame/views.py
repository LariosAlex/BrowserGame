from django.shortcuts import render
from .models import *
# Create your views here.
from django.shortcuts import render
from django.http import HttpRequest
from django.core.exceptions import *
from django.utils import timezone
def vue(request):
    context = {}

    return render(request, 'browserGame/index.html', context)

def landing(request):
    active_season = Season.objects.get(id=1)
    actions = None
    characters = Character.objects.filter(season=active_season).order_by('-level', '-exp')
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
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.http import HttpRequest
from django.core.exceptions import *
def vue(request):
    context = {}

    return render(request, 'browserGame/index.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
    
def landing(request):
    active_season = Season.objects.get(id=11)
    if request.user.is_authenticated:
        try:
            character = Character.objects.get(season=active_season, user=request.user)
        except ObjectDoesNotExist:
            character = None
    else:
        character = None
    print(Character)
    context = {
        'season': active_season,
        'character' : character
    }
    return render(request, 'browserGame/landing.html', context)

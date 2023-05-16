from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django import forms
from django.shortcuts import redirect
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.db.models import Q
from datetime import datetime
from django.utils.timesince import timesince

def getRanking(request):
    season = Season.objects.latest("id")
    characters = list(Character.objects.filter(season=season).order_by('-level', '-exp').values('user__username', 'nickname', 'level'))
    return JsonResponse({"characters": list(characters)})

def getCharacter(request, character_id):
    character = get_object_or_404(Character, pk=character_id)
    character_dict = model_to_dict(character)
    return JsonResponse({"character": character_dict})

def getAction(request, action_id):
    action = get_object_or_404(Action, pk=action_id)
    action_dict = model_to_dict(action)
    return JsonResponse({"action": action_dict}) 


def getActionsLog(request, character_id):
    actions = list(ActionLog.objects.filter(Q(target=character_id) | Q(performer=character_id)).order_by('-datetime').distinct().values('action__category', 'action__name', 'target__nickname', 'performer__nickname', 'succeed', 'datetime')[:25])    
    
    # Formatear la fecha y hora de cada acción
    for action in actions:
        datetime_object = action['datetime']
        formatted_datetime = datetime_object.strftime('%d/%m/%Y %H:%M')
        action['datetime'] = formatted_datetime
        
        # Calcular la diferencia de tiempo entre la acción y la hora actual
        time_since = timesince(datetime_object)
        action['time_since'] = time_since
    
    return JsonResponse({"actions": actions})

def getActions(request):
    actions = list(Action.objects.all().order_by('category').values())
    return JsonResponse({"actions": actions})

def getLastActions(request, character_id):
    user_last_login = Character.objects.filter(pk=character_id).values('user__last_login')
    actions = list(ActionLog.objects.filter(performer=character_id, datetime__gt=user_last_login).order_by('-datetime').distinct().values('action__name', 'datetime', 'action__success_rate', 'run_number', 'succeed', 'performer__nickname'))
    return JsonResponse({"actions": actions})

def getCharacterLogged(request):
    user = request.user
    last_season = Season.objects.last()
    character = Character.objects.filter(user=user, season=last_season).first()
    if character:
        character_dict = model_to_dict(character)
        return JsonResponse({"character": character_dict})
    else:
        return JsonResponse({"character": None})
def getCharacters(request):
    characters = list(Character.objects.all().order_by('level').values())
    return JsonResponse({"characters": characters})

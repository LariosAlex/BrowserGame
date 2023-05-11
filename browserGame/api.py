from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django import forms
from django.shortcuts import redirect
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.db.models import Q

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
    actions = list(ActionLog.objects.filter(Q(target=character_id) | Q(performer=character_id)).order_by('-datetime').distinct().values('action__category', 'action__name', 'target__nickname', 'performer__nickname', 'succeed')[:25])    
    return JsonResponse({"actions": actions})

def getActions(request):
    actions = list(Action.objects.all().order_by('category').values())
    return JsonResponse({"actions": actions})

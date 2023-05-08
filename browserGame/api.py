from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django import forms
from django.shortcuts import redirect
from django.http import JsonResponse
from django.forms.models import model_to_dict

def getRanking(request):
    season = Season.objects.latest("id")
    characters = list(Character.objects.filter(season=season).order_by('-level', '-exp').values())
    return JsonResponse({"characters": list(characters)})

def getCharacter(request, character_id):
    character = get_object_or_404(Character, pk=character_id)
    character_dict = model_to_dict(character)
    return JsonResponse({"character": character_dict})
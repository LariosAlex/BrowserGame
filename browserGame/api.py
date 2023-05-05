from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django import forms
from django.shortcuts import redirect
from django.http import JsonResponse

def getRanking(request):
    season = Season.objects.latest("id")
    characters = list(Character.objects.filter(season=season).order_by('-level', '-exp').values())
    return JsonResponse({
            "status": "OK",
            "characters": characters,
        }, safe=False)
import json

from django.forms import model_to_dict
from .forms import *
from django.shortcuts import render, redirect
from django.contrib.auth.forms import *
from django.contrib.auth import login
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import PasswordResetForm
from .models import *
from django.http import HttpRequest, HttpResponse
from django.core.exceptions import *
from django.utils import timezone
from .utils import save_log
from django.core.mail import send_mail
from django.conf import settings
from django.core import serializers
from django.http import JsonResponse
from datetime import timedelta
from django.shortcuts import get_object_or_404, render

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
            return redirect('password_reset_done')
    else:
        form = PasswordResetForm()
    context = {'form': form}
    return render(request, 'browserGame/password_reset_form.html', context)

def landing(request):
    active_season = Season.objects.latest("id")
    save_log('SQL', 'Season.objects.latest("id")', request)
    save_log('SQL', str(Season.objects.latest("id")), request)
    save_log('INF', 'Accediendo a vista', request)
    if request.user.is_authenticated:
        try:
            character = Character.objects.get(season=active_season, user=request.user)
        except ObjectDoesNotExist:
            character = None
    else:
        character = None
    
    page_data = {"characterLogged": model_to_dict(character)} if character else {}
    context = {
        'season': active_season,
        'character' : character,
        'page_data' : json.dumps(page_data)
    }
    return render(request, 'browserGame/landing.html', context)

def accio(request):
    active_season = Season.objects.latest("id")
    save_log('SQL', 'Season.objects.latest("id")', request)
    save_log('SQL', str(Season.objects.latest("id")), request)
    actions = Action.objects.all()
    characters = Character.objects.filter(season=active_season).order_by('-nickname')
    save_log('SQL', "Character.objects.filter(season=active_season).order_by('-level', '-exp')", request)
    save_log('SQL', str(characters), request)
    save_log('INF', 'Accediendo a vista', request)
    if request.user.is_authenticated:
        try:
            character = Character.objects.get(season=active_season, user=request.user)
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
    return render(request, 'browserGame/actions.html', context)

def save_action(request):
    performer_id = request.POST.get('performer_id')
    if(request.POST.get('target_id') != ""):
        target_id = request.POST.get('target_id')
    else:
        target_id = performer_id
    action_id = request.POST.get('action_id')
    succeed = request.POST.get('succeed')

    if Character.objects.filter(id=performer_id).exists():
        performer = Character.objects.get(id=performer_id)
    else:
        performer = Character.objects.get(id=1)
    if Character.objects.filter(id=target_id).exists():
        target = Character.objects.get(id=target_id)
    else:
        target = Character.objects.get(id=2)
    action = Action.objects.get(id=action_id)
    datetime = timezone.now()

    action_log = ActionLog.objects.create(
        performer=performer,
        target=target,
        action=action,
        succeed=succeed,
        datetime=datetime,
    )

    return JsonResponse({'status': 'ok'})

def damage_character(request):
    id_character = request.POST.get('character_id')
    character = Character.objects.get(id=id_character)
    damage = int(request.POST.get('damage'))
    if(character.life < damage):
        newCharacterLvl = character.level -1
        if(character.level > 1):
            character.level = newCharacterLvl
            character.life = newCharacterLvl*10
            character.mana = newCharacterLvl*10
            character.exp = newCharacterLvl*10
        else:
            character.level = 0
            character.life = 0
            character.mana = 0
            character.exp = 0
    else:
        character.life = character.life - damage
    
    character.save()
    return JsonResponse({'status': 'ok'})

def update_character(request):
    character_id = request.POST.get('character_id')
    character = Character.objects.get(id=character_id)
    
    character.mana = int(request.POST.get('sendMana'))
    character.life = int(request.POST.get('health'))
    character.exp = int(request.POST.get('experience'))
    character.level = int(request.POST.get('level'))
    character.save()
    return JsonResponse({'status': 'ok'})

def activate_cron(request):
    season = Season.objects.latest("id")
    dif_time = timezone.make_aware(datetime.now(), timezone.get_default_timezone()) - season.last_datetime_recharge
    time = season.time_between_recharge
    cantidadDeVecesRecargar = dif_time.total_seconds()//60 *time
    if cantidadDeVecesRecargar >= 1:
        for character in Character.objects.all():
            if character.life > 0:
                if character.level*10 - character.mana > character.level*cantidadDeVecesRecargar:
                    character.mana += character.level*cantidadDeVecesRecargar
                else:
                    character.mana = character.level*10
                character.save()
        
        a = Season.objects.get(id=str(season))
        a.last_datetime_recharge = timezone.make_aware(datetime.now(), timezone.get_default_timezone())
        a.save()

    return HttpResponse('Cron activated!')
 

def ranking(request):
    return render(request, 'browserGame/ranking.html')

def animations(request):
    return render(request, 'browserGame/animations.html')

def actions(request):
    return render(request, 'browserGame/ataques.html')

def userInfo(request, character_name):
    character = Character.objects.get(nickname=character_name)
    season = Season.objects.latest("id")
    characters = list(Character.objects.filter(season=season).order_by('-level', '-exp'))
    character_dict = model_to_dict(character)
    # Obtener el ranking del personaje
    ranking = 0
    for i, c in enumerate(characters):
        if c.id == character.id:
            ranking = i + 1
            break

    character_dict['ranking'] = ranking
    # Obtener el porcentaje de éxito de las acciones del personaje
    success_count = 0
    actions = ActionLog.objects.filter(performer = character)
    for action in actions:
        if action.succeed:
            success_count += 1
    total_actions = actions.count()
    success_percentage = 0
    if total_actions > 0:
        success_percentage = (success_count / total_actions) * 100
    character_dict['success_percentage'] = success_percentage
    context = {'character': character_dict}
    return render(request, 'browserGame/character.html', context)
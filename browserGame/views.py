from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.http import HttpResponse
from .models import Character

def index(request):
    context = {}

    #posar aqui la funcio activate_cron?

    return render(request, 'browserGame/index.html', context)

def activate_cron(request):

    for i in Character.objects.all():
        if i.life > 0:
            if i.level*10 - i.mana > i.level:
                i.mana += i.level
            else:
                i.mana = i.level*10
            i.save()
    
    #data_cron = Seasons.objects.

    return HttpResponse('Cron activated!')


'''
# Obtén el registro que deseas actualizar por su ID
personaje = Personaje.objects.get(id=1)

# Actualiza el valor del atributo deseado
personaje.nombre = 'Nuevo nombre'

# Guarda los cambios en la base de datos
personaje.save()
'''
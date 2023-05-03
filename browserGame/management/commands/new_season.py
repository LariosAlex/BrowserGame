from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from faker import Faker
from random import randint
import random
from datetime import timedelta, datetime
from django.contrib.auth.hashers import make_password


from browserGame.models import *

faker = Faker(["es_CA","es_ES"])

class Command(BaseCommand):
    help = 'Crea joc amb seasons'

    def handle(self, *args, **options):
        print("--CREEM TEMPORADA--")
        season = Season()
        season.game_datetime_starts = datetime.now()
        season.game_datetime_ends = datetime.now() + timedelta(days=1)
        season.time_between_recharge = 60
        diff_seconds = (season.game_datetime_ends - season.game_datetime_starts).total_seconds()
        season.last_datetime_recharge = season.game_datetime_starts + timedelta(seconds=random.randint(0, int(diff_seconds)))
        season.save()

        print("--CREEM USUARIS--")
        for i in range(8):
            personajes = ['Vaquero', 'Sheriff', 'Bandido', 'Forajido', 'Explorador', 'Ganadero', 'Pistolero', 'Minero', 'Juez', 'Indio', 'Bandolero', 'Carroñero', 'Cazador de recompensas', 'Leñador', 'Granjero', 'Proveedor', 'Banquero', 'Misionero', 'Empresario ferroviario', 'Fronterizo']
            name = faker.first_name()
            last_name = faker.last_name()
            password = make_password(name+'1234')
            user = User(username=name+'_'+last_name,first_name=name, last_name=last_name, password=password)
            user.save()            
            print('--Creeem personatge per a: '+user.username+'--')
            character = Character()
            character.user = user
            character.season = season
            character.nickname = f"{random.choice(personajes).capitalize()} {faker.first_name().capitalize()}"
            lvl = random.randint(1, 10)
            character.level = lvl
            character.life = random.randint(1, (lvl*10))
            character.mana = random.randint(0, (lvl*10))
            character.exp = random.randint(0, (lvl*10)-1)
            character.save()
        
        for i in range(30):
            action = Action()
            OFF = ['Disparar', 'Acuchillar', 'Golpear', 'Lanzar', 'Embestir', 'Aplastar', 'Disparar flechas', 'Empujar', 'Lanzar lazo', 'Intimidar']
            DEF = ['Esquivar', 'Bloquear', 'Parar', 'Correr', 'Agacharse', 'Saltar', 'Rodar', 'Desarmar', 'Luchar cuerpo a cuerpo', 'Gritar']
            PAS = ['Descansar', 'Consumir', 'Dormir', 'Socializar', 'Explorar', 'Vigilar', 'Acariciar', 'Aseo', 'Observar', 'Revisar']
            typeOfAction = ['DEF','OFF','PAS']
            action.category = random.choice(typeOfAction)
            action.damage = 0
            action.health = 0
            action.mana = 0
            if action.category == 'OFF':
                action.name = random.choice(OFF)
                action.damage = random.randint(10, 50)
            elif action.category == 'DEF':
                action.name = random.choice(DEF)
                action.health = random.randint(10, 50)
            else: 
                action.name = random.choice(PAS)
                action.mana = random.randint(1, 10)
            action.success_rate = random.randint(10, 100)
            action.exp = random.randint(10, 50)
            action.cost = random.randint(1, 20)
            action.save()
        
        for character in Character.objects.filter(season=season):
            for i in range(10):
                ch_action = ActionLog()
                ch_action.performer = character
                rand_action = Action.objects.order_by("?").first()
                ch_action.action = rand_action
                successfully = [True, False]
                if rand_action.category == 'OFF':
                    ch_action.target = Character.objects.filter(season=season).order_by("?").first()
                else:
                    ch_action.target = character
                ch_action.succeed = random.choice(successfully)
                ch_action.datetime = datetime.now()
                ch_action.save()
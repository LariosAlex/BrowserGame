from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from faker import Faker
from random import randint
import random
from datetime import timedelta, datetime


from browserGame.models import *
from django.contrib.auth.models import User

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
            animals = ['cat', 'dog', 'elephant', 'lion', 'tiger', 'bear', 'giraffe', 'zebra', 'hippopotamus', 'rhinoceros', 'monkey', 'crocodile', 'snake', 'lizard', 'turtle', 'kangaroo', 'penguin', 'panda', 'koala', 'wolf', 'fox', 'deer', 'rabbit', 'hamster', 'mouse', 'guinea pig', 'parrot', 'seagull', 'octopus', 'shark']
            name = faker.first_name()
            last_name = faker.last_name()
            user = User(username=name+'_'+last_name,first_name=name, last_name=last_name)
            user.save()            
            print('--Creeem personatge per a: '+user.username+'--')
            character = Character()
            character.user = user
            character.season = season
            character.nickname = f"{faker.color_name().capitalize()} {random.choice(animals).capitalize()}"
            lvl = random.randint(1, 10)
            character.level = lvl
            character.life = random.randint(1, (lvl*10))
            character.mana = random.randint(0, (lvl*10))
            character.exp = random.randint(0, (lvl*10)-1)
            character.save()
        
        for i in range(30):
            action = Action()
            animals = ['cat', 'dog', 'elephant', 'lion', 'tiger', 'bear', 'giraffe', 'zebra', 'hippopotamus', 'rhinoceros', 'monkey', 'crocodile', 'snake', 'lizard', 'turtle', 'kangaroo', 'penguin', 'panda', 'koala', 'wolf', 'fox', 'deer', 'rabbit', 'hamster', 'mouse', 'guinea pig', 'parrot', 'seagull', 'octopus', 'shark']
            action.name = random.choice(animals).capitalize()
            typeOfAction = ['DEF','OFF','PAS']
            action.category = random.choice(typeOfAction)
            action.success_rate = random.randint(10, 100)
            action.exp = random.randint(10, 50)
            action.damage = random.randint(10, 50)
            action.health = random.randint(10, 50)
            action.mana = random.randint(1, 20)
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
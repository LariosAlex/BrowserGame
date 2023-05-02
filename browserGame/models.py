from django.db import models
from django.contrib.auth.models import AbstractUser, User
from datetime import datetime, timedelta
from django.contrib import admin
from django.utils import timezone

class User(AbstractUser):
    last_login = models.DateTimeField(default=timezone.now)

    def get_all_actions(self):
        character_ids = self.characters.values_list('id', flat=True)
        actions = ActionLog.objects.filter(character_id__in=character_ids)[:10]
        return actions

class Season(models.Model):
    game_datetime_starts = models.DateTimeField()
    game_datetime_ends = models.DateTimeField()
    time_between_recharge = models.IntegerField()
    last_datetime_recharge = models.DateTimeField()
    def __str__(self):
        return str(self.id)
    
    def time_until_next_recharge(self):
        now = timezone.make_aware(datetime.now(), timezone.get_default_timezone())
        next_recharge = self.last_datetime_recharge + timedelta(minutes=self.time_between_recharge)
        time_left = next_recharge - now
        return time_left

class Character(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=255)
    life = models.IntegerField()
    mana = models.IntegerField()
    level = models.IntegerField()
    exp = models.IntegerField()
    def __str__(self):
        return self.nickname


class Action(models.Model):
    TYPE_ACTION = (
        ('DEF', 'Defensive'),
        ('OFF', 'Offensive'),
        ('PAS', 'Passive'),
    )
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=4, choices=TYPE_ACTION)
    mana = models.IntegerField()
    success_rate = models.IntegerField()
    exp = models.IntegerField()
    damage = models.IntegerField()
    health = models.IntegerField()
    def __str__(self):
        return self.name


class ActionLog(models.Model):
    performer = models.ForeignKey(Character, related_name='performer', on_delete=models.CASCADE)
    target = models.ForeignKey(Character, related_name='target', on_delete=models.CASCADE)
    action = models.ForeignKey(Action, on_delete=models.CASCADE)
    succeed = models.BooleanField()
    datetime = models.DateTimeField()
    def __str__(self):
        return self.performer.nickname+'--'+str(self.succeed)

class Log(models.Model):
    TYPE_CHOICES = (
        ('INF', 'Information'),
        ('WAR', 'Warning'),
        ('ERR', 'Error'),
        ('FAT', 'Fatal'),
        ('SQL', 'SQL'),
    )
    type_log = models.CharField(max_length=4, choices=TYPE_CHOICES)
    current_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    message = models.CharField(max_length=255)
    document = models.CharField(max_length=255, blank=True, null=True)
    line = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.type_log

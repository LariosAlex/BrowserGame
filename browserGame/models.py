from django.db import models
from django.contrib.auth.models import User

class Season(models.Model):
    game_datetime_starts = models.DateTimeField()
    game_datetime_ends = models.DateTimeField()
    time_between_recharge = models.IntegerField()
    last_datetime_recharge = models.DateTimeField()

class Character(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=255)
    life = models.IntegerField()
    mana = models.IntegerField()
    level = models.IntegerField()
    exp = models.IntegerField()

class Action(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    cost = models.IntegerField()
    success_rate = models.IntegerField()
    e_points = models.IntegerField()
    d_points = models.IntegerField()
    h_points = models.IntegerField()

class ActionLog(models.Model):
    attacker = models.ForeignKey(User, related_name='attacker', on_delete=models.CASCADE)
    victim = models.ForeignKey(User, related_name='victim', on_delete=models.CASCADE)
    action = models.ForeignKey(Action, on_delete=models.CASCADE)
    succeed = models.BooleanField()
    datetime = models.DateTimeField()

class Log(models.Model):
    TYPE_CHOICES = (
        ('INF', 'Information'),
        ('WAR', 'Warning'),
        ('ERR', 'Error'),
        ('FAT', 'Fatal'),
    )
    type = models.CharField(max_length=4, choices=TYPE_CHOICES)
    current_time = models.DateTimeField(auto_now_add=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    failed_document = models.CharField(max_length=255, blank=True, null=True)
    failed_line = models.IntegerField(blank=True, null=True)
    user_admin = models.ForeignKey(User, related_name='admin', on_delete=models.CASCADE)
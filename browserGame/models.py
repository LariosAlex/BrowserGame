from django.db import models
from django.contrib.auth.models import User

class Season(models.Model):
    game_datetime_starts = models.DateTimeField()
    game_datetime_ends = models.DateTimeField()
    time_between_recharge = models.IntegerField()
    last_datetime_recharge = models.DateTimeField()
    def __str__(self):
        return str(self.id)

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
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    mana = models.IntegerField()
    success_rate = models.IntegerField()
    experience = models.IntegerField()
    damage = models.IntegerField()
    health = models.IntegerField()

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
    type_log = models.CharField(max_length=4, choices=TYPE_CHOICES)
    current_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    failed_document = models.CharField(max_length=255, blank=True, null=True)
    failed_line = models.IntegerField(blank=True, null=True)
from django.contrib import admin
from .models import *
from django.utils.timesince import timesince

class UserActionsInline(admin.TabularInline):
    model = ActionLog
    extra = 0
    fk_name = 'performer'
    
class CharactersAdmin(admin.ModelAdmin):
    inlines = [UserActionsInline]

class UserCharactersInline(admin.TabularInline):
    model = Character
    extra = 0
    inlines = [UserActionsInline]
    fields = ['nickname', 'season', 'level']
    readonly_fields = fields

class UserLogsInline(admin.TabularInline):
    model = Log
    extra = 0
    fields = ['type_log', 'message']
    readonly_fields = fields

class UserAdmin(admin.ModelAdmin):
    fields = ['username', 'first_name', 'last_name', 'email', 'password', 'last_login', 'time_since_last_login']
    readonly_fields = ('time_since_last_login',)
    inlines = [UserCharactersInline, UserLogsInline]
    list_per_page = 25
    
    def time_since_last_login(self, obj):
        return timesince(obj.last_login)
    
    time_since_last_login.short_description = 'Time since last login'
    
    def save_model(self, request, obj, form, change):
        obj.set_password(form.cleaned_data["password"])
        super().save_model(request, obj, form, change)

class LogsAdmin(admin.ModelAdmin):
    list_per_page = 25
    readonly_fields = [field.name for field in Log._meta.get_fields()]
    
    def time_since_log(self, obj):
        return timesince(obj.current_time)
    
    readonly_fields += ['time_since_log']
    time_since_log.short_description = 'Time since log'

class UserAdmin(admin.ModelAdmin):
    fields = ['username', 'first_name', 'last_name', 'email', 'password', 'last_login', 'time_since_last_login']
    readonly_fields = ('time_since_last_login',)
    inlines = [UserCharactersInline, UserLogsInline]
    list_per_page = 25
    
    def time_since_last_login(self, obj):
        return timesince(obj.last_login)
    
    time_since_last_login.short_description = 'Time since last login'


class SeasonAdmin(admin.ModelAdmin):
    list_display = ['id', 'game_datetime_starts', 'game_datetime_ends', 'last_datetime_recharge', 'time_until_next_recharge', 'time_between_recharge', 'time_since_game_datetime_starts', 'time_since_game_datetime_ends' , 'time_since_last_datetime_recharge']
    readonly_fields = ('time_since_game_datetime_starts', 'time_since_game_datetime_ends' , 'time_since_last_datetime_recharge', 'time_until_next_recharge')

    def time_since_game_datetime_starts(self, obj):
        return timesince(obj.game_datetime_starts)
    
    def time_since_game_datetime_ends(self, obj):
        return timesince(obj.game_datetime_ends)
    
    def time_since_last_datetime_recharge(self, obj):
        return timesince(obj.last_datetime_recharge)
    
    def time_until_next_recharge(self, obj):
        now = timezone.make_aware(datetime.now(), timezone.get_default_timezone())
        next_recharge = obj.last_datetime_recharge + timedelta(minutes=obj.time_between_recharge)
        time_left = next_recharge - now
        return time_left
    
    time_since_game_datetime_starts.short_description = 'Time since game start'
    time_since_game_datetime_ends.short_description = 'time since game end'
    time_since_last_datetime_recharge.short_description = 'Time since the last recharge'
    time_until_next_recharge.short_description = 'Time until next recharge'

class ActionLogAdmin(admin.ModelAdmin):
    readonly_fields = (['time_since_datetime'])
    def time_since_datetime(self, obj):
        return timesince(obj.datetime)
    time_since_datetime.short_description = 'Time since log'

admin.site.register(User, UserAdmin)
admin.site.register(Season, SeasonAdmin)
admin.site.register(Character, CharactersAdmin)
admin.site.register(Action)
admin.site.register(ActionLog, ActionLogAdmin)
admin.site.register(Log, LogsAdmin)

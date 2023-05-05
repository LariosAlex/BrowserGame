from django.contrib import admin
from .models import *


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
    fields = ['username', 'first_name', 'last_name', 'email', 'password', 'last_login']
    inlines = [UserCharactersInline, UserLogsInline]
    list_per_page = 25
    def save_model(self, request, obj, form, change):
        obj.set_password(form.cleaned_data["password"])
        super().save_model(request, obj, form, change)

class LogsAdmin(admin.ModelAdmin):
    list_per_page = 25
    readonly_fields = [field.name for field in Log._meta.get_fields()]

admin.site.register(User, UserAdmin)
admin.site.register(Season)
admin.site.register(Character, CharactersAdmin)
admin.site.register(Action)
admin.site.register(ActionLog)
admin.site.register(Log, LogsAdmin)

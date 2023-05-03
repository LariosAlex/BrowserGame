from django.contrib import admin
from .models import *


class CharactersActionsInline(admin.TabularInline):
    model = ActionLog
    extra = 0
    fk_name = 'performer'
    
class CharactersAdmin(admin.ModelAdmin):
    inlines = [CharactersActionsInline]

class CharactersInline(admin.TabularInline):
    model = Character
    extra = 0
    inlines = [CharactersActionsInline]
    fields = ['nickname', 'season', 'level']
    readonly_fields = fields

class UserAdmin(admin.ModelAdmin):
    fields = ['username', 'first_name', 'last_name', 'email', 'password', 'last_login']
    inlines = [CharactersInline]
    list_per_page = 25
    def save_model(self, request, obj, form, change):
        obj.set_password(form.cleaned_data["password"])
        super().save_model(request, obj, form, change)

class LogsAdmin(admin.ModelAdmin):
    list_per_page = 25

admin.site.register(User, UserAdmin)
admin.site.register(Season)
admin.site.register(Character, CharactersAdmin)
admin.site.register(Action)
admin.site.register(ActionLog)
admin.site.register(Log, LogsAdmin)

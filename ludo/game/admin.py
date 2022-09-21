from django.contrib import admin

from . models import Game, Gamelist

# Register your models here.
class GameAdmin(admin.ModelAdmin):
    list_display = ['sport_type', 'date','arranger']
    search_fields = ['sender', 'receiver', 'game']


admin.site.register(Game, GameAdmin)
admin.site.register(Gamelist)
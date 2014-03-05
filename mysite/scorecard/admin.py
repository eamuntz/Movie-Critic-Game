from django.contrib import admin
from scorecard.models import Player

class PlayerAdmin(admin.ModelAdmin):
	fields = ['name','score']
	list_display = ('name','score')

admin.site.register(Player, PlayerAdmin)
# Register your models here.

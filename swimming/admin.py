from django.contrib import admin
from swimming.models import Team, Athlete


class TeamAdmin(admin.ModelAdmin):
    search_fields = ('name',)


class AthleteAdmin(admin.ModelAdmin):
    search_fields = ('name',)


admin.site.register(Team, TeamAdmin)
admin.site.register(Athlete, AthleteAdmin)

from django.contrib import admin
from .models import Event

class EventsAdmin(admin.ModelAdmin):
    list_display = ("celebrant", "birthdate")
    prepopulated_fields = {"slug": ("celebrant",)} 
admin.site.register(Event)
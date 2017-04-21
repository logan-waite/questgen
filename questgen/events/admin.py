from django.contrib import admin

from .models import Event_Type, Event, Action

# Register your models here.
admin.site.register(Event_Type)
admin.site.register(Event)
admin.site.register(Action)

from django.contrib import admin

from .models import Character_Type, Character, Dialogue, Response

# Register your models here.
admin.site.register(Character_Type)
admin.site.register(Character)
admin.site.register(Dialogue)
admin.site.register(Response)

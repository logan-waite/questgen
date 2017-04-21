from django.contrib import admin

from .models import Meter, Player, Player_Meter

# Register your models here.
admin.site.register(Meter)
admin.site.register(Player)
admin.site.register(Player_Meter)

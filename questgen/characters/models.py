from django.db import models

from player.models import Meter

# Create your models here.
class Character_Type(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

class Character(models.Model):
    name = models.CharField(max_length=50)
    character_type = models.ForeignKey(Character_Type)

    def __str__(self):
        return str(self.name)

class Dialogue(models.Model):
    player = models.ForeignKey(Character)
    content = models.TextField()

    def __str__(self):
        return str(self.content)

class Response(models.Model):
    dialogue = models.ForeignKey(Dialogue)
    content = models.CharField(max_length=50)
    meter = models.ForeignKey(Meter)
    meter_value = models.IntegerField()

    def __str__(self):
        return str(self.content)

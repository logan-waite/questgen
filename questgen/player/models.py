from django.db import models

# from games.models import Game

# Create your models here.
class Meter(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

class Player(models.Model):
    name = models.CharField(max_length=50)
    story_counter = models.IntegerField()
    # game = models.ForeignKey(Game)

    def __str__(self):
        return str(self.name)

class Player_Meter(models.Model):
    player = models.ManyToManyField(Player)
    meter = models.ManyToManyField(Meter)
    status = models.IntegerField()

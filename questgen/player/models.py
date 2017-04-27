from django.db import models

from games.models import Game, Meter

# Create your models here

class Player(models.Model):
    name = models.CharField(max_length=50)
    story_counter = models.IntegerField(default=0)
    game = models.ForeignKey(Game)
    meters = models.ManyToManyField(Meter, through="Player_Meter")

    def __str__(self):
        return str(self.name)

class Player_Meter(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    meter = models.ForeignKey(Meter, on_delete=models.CASCADE)
    status = models.IntegerField()

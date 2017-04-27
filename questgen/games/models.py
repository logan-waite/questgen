from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('auth.User', related_name='games')

    def __str__(self):
        return str(self.name)

class Meter(models.Model):
    name = models.CharField(max_length=50)
    game = models.ForeignKey(Game)

    def __str__(self):
        return str(self.name)

class Settings(models.Model):
    game = models.ForeignKey(Game)
    story_event_probability = models.IntegerField()
    max_event_length = models.IntegerField()
    min_event_length = models.IntegerField()

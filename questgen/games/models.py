from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=50)

class User_Game(models.Model):
    user = models.ManyToManyField(User)
    game = models.ManyToManyField(Game)
